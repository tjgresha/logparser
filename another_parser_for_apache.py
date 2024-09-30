import re

with open('access.log', 'r') as file:
    for line in file:
        match = re.search(r'(\d+\.\d+\.\d+\.\d+).*"GET (.+?) HTTP', line)
        if match:
            ip_address = match.group(1)
            requested_url = match.group(2)
            print(f'IP: {ip_address}, URL: {requested_url}')
