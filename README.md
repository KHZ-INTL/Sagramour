# Sagramour

An image scraper script written in python 3.x that utilises Tuchong and Androidesk web API


## Dependencies
- Requests
- Flask
- Json

## Usage:
 1. Run the script and it will spawn a local webserver on 127.0.0.1:5000 or localhost:5000
 2. Search for images:
      - Append "/" and your search term to the URL:
      - <Protocol><webserver(port)>/<searchTerm>/<page>   //the page paramater can be omitted
      - example" http://127.0.0.1:5000/flowers/2

## Aditional Notes
   - You can uncomment and adjust the code for Tuchong parsing section to only allow photos with certian height or width.
