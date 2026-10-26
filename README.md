### Web Scraping & Data Engineering Pipeline: Quotes to Scrape

A complete data engineering pipeline built to scrape, clean, and normalise unstructured web data, preparing it for downstream business intelligence analytics. 

This project demonstrates the core phases of data engineering: automated web crawling, local CSV staging, defensive data cleaning, and calculated metric engineering. 

### Project Data Architecture

The pipeline processes data through a structured staging and transformation architecture: 

Live Website (HTML)
│
▼  [ Scrapy Framework Spider ]
my_quotes.csv (Raw Staging File)
│
▼  [ Python Data Cleansing & Metric Engineering ]
clean_csv.py (Transformation Script Engine)
│
▼  [ Native Python csv module ]
clean_quotes.csv ➔ Uploaded to Excel for the Web 

### 🛠️ Data Engineering Phases

### Phase 1: Web Scraping & Ingestion

The scraper (quotes_spider.py) runs live on the internet using the Scrapy framework. 

* Extracts Quote Text, Author Name, and Tags.
* Implements multi-page extraction by programmatically identifying and recursively following the ul.pager li.next a navigation links across all 10 pages of the website.
* Persists the extracted raw dataset into a local my_quotes.csv file.

### Phase 2: Data Cleansing & Metric Engineering

The data cleansing operations stage a clean data schema. The pipeline performs defensive cleaning on hidden website inconsistencies: 

* Text Normalisation: Removes inconsistent double quotation marks (") embedded unevenly in the web text using text replacement logic.
* Whitespace Pruning: Shaves off trailing or leading blank space variations using string trimming methods so categorical fields group cleanly in analytics graphics.
* Calculated Metric Engineering: The pipeline dynamically calculates the exact text length metrics programmatically by measuring the total character count minus the length of the string without spaces, offset by one to calculate the exact word metrics.
* Filter Guardrails: Eliminates system null values or completely blank space rows using strict gatekeeping rules.

-- now the pipeline removes the original messy double quotes scraped from the websites HTML markup and clean_quotes.csv will add its own structural double quotes around sentences with commas to prevent text spilling into the wrong spreadsheet columns. 

### Phase 3: Production Flat-File Export

To support spreadsheet analysis, a lightweight script (clean_csv.py) extracts the cleaned data back into a flat file. 

* **Native Processing:** Uses 100% native Python without heavy external libraries like pandas.
* **Excel Compatibility:** Automatically handles string encapsulations so text fields open perfectly inside **Excel for the Web** on any platform (Mac/Windows) without breaking spreadsheet columns.

### How to Run the Pipeline

### 1. Execute the Web Scraper

Generate the raw CSV data from the live internet: 

bash

python3 -m scrapy runspider quotes_spider.py -o my_quotes.csv


### 2. Execute the Cleansing Engine

Ingest the raw data, run data cleansing operations, and engineer the polished tables: 

bash

python3 clean_csv.py

### 3. Terminal Data Verification

Inspect the compiled results inside your production tables using your command line tools: 

bash

head -n 5 clean_quotes.csv


The finalized asset clean_quotes.csv stands completely prepped for import. Future metrics mapped out for dashboard development include: 

* Author Frequency Visuals: Top-performing quote engines.
* Topic Slicers: Grouping interactive charts based on split-semicolon tags.
* Calculated Metrics Analysis: Evaluating average quote length by author using the custom word count metric.