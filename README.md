# HAR-file-analysis
HAR file is important for web application development, debugging, and troubleshooting

A HAR (HTTP Archive) file is crucial for web application development, debugging, and troubleshooting because it captures a detailed log of a web browser's interactions with a website. The developers, QA team, and testing team can gain insight into network behavior to enhance problem resolution, data pass in network, and reporting problems accurately and cross-team collaboration effectively. It equally offers benefits to security personnel.

For diagnosing issues and optimizing the performance of web applications, HAR files stand out as a valuable tool for optimizing performance of web applications.

## What is a HAR File and what does it contain?

A HAR file is a JSON-formatted archive file that records network activities during a web session. It captures comprehensive data about each network request and response, including URLs, HTTP methods, status codes, headers, bodies, timing information, and cookies.

**Detailed Network Logging:** A HAR file captures network requests and responses, including headers, cookies, payloads, response, and timing information. This comprehensive logging helps to see exactly what happens behind the scenes during a web session.</li>

**Performance Metrics:** A HAR file includes detailed timing data, such as DNS lookup time, TCP handshake time, request and response time, and total load time. This allows to identify performance bottleneck, and optimize page load speeds.

## Benefit of HAR file

**Detailed Issue Reporting:** When support teams encounter problems, they can generate and share a HAR file with developers. It eliminates back-and-forth communications and reduces time to resolve issues. A HAR file captures every request and response made by the web browser. This is crucial for debugging complex interactions that involve multiple API calls and resource loads.

**Collaboration Across Teams:** HAR file serves as a common reference point for developers, QA testers, and support teams. It facilitates better collaboration and understanding across different teams working on the same project.

**Security Analysis:** By analyzing a HAR file, the security team can inspect data exchange between the web browser and a server, identify potentially sensitive data being transmitted, such as personal information or authentication tokens, and ensure that data is properly protected. It enables them to identify potential security vulnerabilities such as unencrypted data transmission, insecure cookies, suspicious network requests and HTTP headers etc. By analyzing a HAR file, security teams can assess the security posture of a web application and take proactive measures to mitigate risks and strengthen defenses.

**Performance Optimization:** Developers can use HAR file to identify slow-loading resources and optimize them for faster page loads, improving the overall user experience.

## Generate HAR File

Generating a HAR file is done using the developer tools in web browsers. Here's how you can create a HAR file in Chrome or Edge or Firefox

>Open Chrome and navigate to the webpage you want to analyze.  
Open Developer Tools (Right-click on the page > Inspect > Network tab) or use Ctrl+Shift+INote: it is "inspect Element" in Mozilla.  
Reload the page to capture all network requests.  
Right-click within the Network tab and select "Save all as HAR with content".  
Save the HAR file to your computer.  

While developing or debugging a web application from a Web Browser, one can open "Developer tool" and monitor network interaction and its behavior.

## Security Considerations - Sanitizing HAR file

HAR file can contain sensitive information, such as cookies and authentication tokens. Always sanitize HAR file before sharing; protect confidential data.

### Sanitizing manually

Open the HAR File: HAR file is JSON file, so you can open it with any text editor.

Locate Confidential Information: Search for sensitive information such as "Authorization", "Cookie", or any other headers or fields that might contain credentials or personal data.

Remove or Mask Confidential Information: Delete the values of these sensitive fields or replace them with another text.

Save the Edited HAR File: Save the changes to the HAR file after removing or masking the confidential information.

### Sanitizing using tool

If you have Node.js installed, you can use  har-sanitizer to automatically remove sensitive information

```
npm install -g har-sanitizer
har-sanitizer -i input.har -o output.har
```

### Best practice:

_While certain types of data may universally be considered sensitive (e.g., personal identifiable information), the specific categories or criteria for what constitutes sensitive data may differ depending on the organization's industry, regulatory requirements, and internal policies. Therefore, the best practice is to perform a manual review of the sanitized file. This ensures that all proprietary, personal, and sensitive information is thoroughly removed, aligning with your organization's specific privacy and security policies. Manual verification adds an essential layer of scrutiny that automated processes might miss, thereby safeguarding against inadvertent data exposure. You can develop your own sanitize API based on the need._


## Enhance readability - View HAR file as HTML

Converting a HAR file to HTML provides a structured, accessible, and flexible way to analyze and share network activity data. It transforms raw JSON data into a format that is more user-friendly, allowing for better insights and effective communication.


## The Code to convert HAR file to HTML
Please find a sample code, it is one of the many ways to convert an HAR file to HTML.  
We will be using **Python**, so let install jinja2
```
pip install jinja2
```

>Jinja2 is commonly used for rendering HTML templates.

***The Python code.***

```
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

```

***The HTML Template file***

```
<!-- Template.html file. You can design your own-->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>HAR File Report</title>
    <style>
        table {
            width: 90%;
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid black;
            padding: 4px;
            text-align: left;
			word-wrap: break-word;
        }
        th {
            background-color: #f2f2f2;
        }
    </style>
</head>
<body>
    <h1>HAR File Report</h1>
    <table>
        <tr>
            <th>URL</th>
            <th>Status</th>
            <th>Time (ms)</th>
            <th>Method</th>
        </tr>
        {% for entry in entries %}
        <tr>
            <td><div style = "width:500px; word-wrap: break-word">{{ entry.request.url }}</div></td>
            <td>{{ entry.response.status }}</td>
            <td>{{ entry.time }}</td>
            <td>{{ entry.request.method }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
```

