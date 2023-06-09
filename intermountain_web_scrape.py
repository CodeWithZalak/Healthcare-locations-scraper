import requests
from bs4 import BeautifulSoup
import pandas as pd

class Intermountain():  
    def __init__(self):
        self.hospital_list = []

    def pagination(self):  
        url = f'https://intermountainhealthcare.org/locations/search-results/'
        
        while True:
            print(url)
            url = self.serach_page_scrape(url)
            if url is None:
                break

    def serach_page_scrape(self,url):
        
        response = requests.get(url)
        soup = BeautifulSoup(response.text , 'html.parser')
        box = soup.find('div',class_="locations__inner")
        hospitals =box.find_all('header',class_="card-location__header")
        for hospital in hospitals:
            hospital_list_data = self.hospital_info(hospital)
            self.hospital_list.append( hospital_list_data)


        page_tags = soup.find('div', class_='pagination').find_all('li')
       

        pages = {
            tag.span.text.strip().lower(): f'https://intermountainhealthcare.org{tag.a.get("href")}'
            for tag
            in page_tags
            if tag.span
        }
        return pages.get('next')
    
    def hospital_info(self,hospital):
        name = hospital.find('h3',class_="card-location__heading").a.span.text
        url = 'https://intermountainhealthcare.org' + hospital.find('a', {'itemprop': 'url'}).get('href')

        latitude = hospital.find('meta', {'itemprop': 'latitude'}).get('content')
        longitude = hospital.find('meta', {'itemprop': 'longitude'}).get('content')


        street_1 = hospital.find('span',class_="meta-item__street-address1").text.strip()
        street_2 = hospital.find('span',class_="meta-item__street-address2").text.strip()
        city = hospital.find('span',class_="meta-item__locality").text.strip().strip(',')
        state = hospital.find('span',class_="meta-item__region").text.strip().strip(',')
        zip_code = hospital.find('span',class_="meta-item__postal-code").text.strip().strip(',')
        
        try:
            phone = hospital.find('span',{"itemprop":"telephone"}).text.strip()
        except:
            phone = "Na"
        
        try:
            fax = hospital.find('span',{'itemprop':"fax"}).text.strip()
        except:
            fax = 'Na'

        hospital_data = {'name': name,
                         'latitude': latitude,
                         'longitude': longitude,
                         'street_1': street_1,
                         'street_2': street_2,
                         'city': city,
                         'state': state,
                         'zip-code': zip_code,
                         'phone': phone,
                         'fax': fax,
                         'url': url }
        
        return hospital_data
    
    def to_dataframe(self):    
        df = pd.DataFrame(self.hospital_list)
        df.to_csv('Hospital_imformations.csv')
    
    def main(self):
        self.pagination()
        self.to_dataframe()

if __name__ == '__main__':
    Intermountain().main()
            
