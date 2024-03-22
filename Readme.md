# Web Page Fetcher
This is a command-line program that fetches web pages and saves them to disk for later retrieval and browsing.

## Usage
To use the program, run the following command:

```
python fetch.py <url1> <url2> ...
```
You can specify as many URLs as you want. The program will download the HTML content of each URL and save it to a file in the current directory.

If any errors occur during the download process, the program will print the error to the console.

## Metadata
The program also records metadata about the fetched content, including:

Date and time of the last fetch
Number of links on the page
Number of images on the page
After fetching the web pages, the program will print this metadata to the console.

## Building and Running
To build and run the program, use the provided Dockerfile. Make sure Docker is installed on your machine.

Build the Docker image:

``` 
docker build -t web_page_fetcher .
```
Run the Docker container:

``` 
docker run web_page_fetcher <url1> <url2> ... 
```