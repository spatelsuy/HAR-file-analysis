# This script converts a HAR (HTTP Archive) file into an HTML file 
# using the Jinja2 templating engine. The script reads the HAR file, 
# processes the network request/response data, 
# and outputs a formatted HTML report.
#
# Requirements
# Python 3.x
# jinja2 library
# pip install jinja2

import json
from jinja2 import Environment, FileSystemLoader

def convert_har_to_html(har_file, output_file):
    # Load the HAR data
    with open(har_file, encoding="utf8") as file:
        har_data = json.load(file)
    
    # Extract entries
    entries = har_data['log']['entries']
    
    # Load the template
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('Template.html')
    
    # Render the HTML
    html_content = template.render(entries=entries)
    
    # Save the output
    with open(output_file, 'w') as file:
        file.write(html_content)
    print(f'Converted {har_file} to {output_file}')

if __name__ == "__main__":
    input_har_file = "input.har"
    output_html_file = "output.html"
    convert_har_to_html(input_har_file, output_html_file)
