import argparse
from google_dork import GoogleDork

def main():
    parser = argparse.ArgumentParser(description="Google Dorking CLI Tool without API")
    parser.add_argument("-d", "--domain", type=str, help="Domain to target, e.g., example.com")
    parser.add_argument("-f", "--filetype", type=str, help="Filetype to search, e.g., pdf, xlsx")
    parser.add_argument("-t", "--intext", type=str, help="Text to search within files, e.g., sensitive data")
    parser.add_argument("-i", "--intitle", type=str, help="Title text to search, e.g., login page")
    parser.add_argument("-u", "--inurl", type=str, help="URL text to search, e.g., admin")

    args = parser.parse_args()

    dork = GoogleDork(
        domain=args.domain,
        filetype=args.filetype,
        intext=args.intext,
        intitle=args.intitle,
        inurl=args.inurl
    )

    results = dork.search()
    dork.display_results(results)

if __name__ == "__main__":
    main()
