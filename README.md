# Healthcare-locations-scraper


This is a web scraping project that extracts hospital information from the Intermountain Healthcare website. It retrieves details such as the name, address, contact information, and geographical coordinates of various hospitals within the Intermountain Healthcare network.

## Overview

The Intermountain Healthcare Locations Scraper is a Python script that utilizes the `requests` and `BeautifulSoup` libraries to scrape data from the Intermountain Healthcare website. The script navigates through the search results pages, extracts information about each hospital, and stores the data in an Excel file.

## Prerequisites

Before running the script, ensure that you have the following dependencies installed:

- Python 3.x
- requests library
- BeautifulSoup library
- pandas library

You can install the required libraries by running the following command:

pip installrequests beautifulsoup4 pandas

## Usage

1. Clone the repository to your local machine using the following command:

      git clone https://github.com/CodeWithZalak/intermountain-hospitals-scraper.git

2. Navigate to the project directory:

      cd intermountain-hospitals-scraper

3. Run the script:

      python scraper.py


The script will start scraping the Intermountain Healthcare website and display the progress. Once the scraping is complete, it will generate an Excel file named `Hospital_information.xlsx` containing the extracted hospital data.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request. Please ensure that you follow the repository's code of conduct.

## License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute the code for both commercial and non-commercial purposes.

## Disclaimer

The data scraped using this script is solely for informational purposes. Please refer to the [Intermountain Healthcare](https://intermountainhealthcare.org/) website for the most up-to-date and accurate information about their hospitals and healthcare services.
