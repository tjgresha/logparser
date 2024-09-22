import re
from collections import namedtuple

LogEntry = namedtuple('LogEntry',['ip', 'datetime', 'method', 'url', 'http_version', 'status', 'size'])

logPatter = re.compile 



log_pattern = re.compile(
    r'(?P<ip>\S+) '               # IP Address
    r'\S+ \S+ '                    # Unused fields (dash fields)
    r'\[(?P<datetime>[^\]]+)\] '   # Date and time
    r'"(?P<method>\S+) '           # HTTP method (GET, POST, etc.)
    r'(?P<url>\S+) '               # Requested URL
    r'HTTP/(?P<http_version>\S+)" ' # HTTP version
    r'(?P<status>\d+) '            # Status code
    r'(?P<size>\S+)'               # Response size
)

# Function to parse a log line
def parse_log_line(line):
    match = log_pattern.match(line)
    if match:
        # Extract data and return it as a LogEntry
        return LogEntry(
            ip=match.group('ip'),
            datetime=match.group('datetime'),
            method=match.group('method'),
            url=match.group('url'),
            http_version=match.group('http_version'),
            status=int(match.group('status')),
            size=match.group('size') if match.group('size') != '-' else 0  # Handle missing size
        )
    else:
        return None

# Function to parse an entire log file
def parse_log_file(file_path):
    log_entries = []
    
    # Read the log file line by line
    with open(file_path, 'r') as f:
        for line in f:
            parsed_line = parse_log_line(line)
            if parsed_line:
                log_entries.append(parsed_line)
    
    return log_entries

# Sample log for demonstration
log_file = """127.0.0.1 - - [22/Sep/2024:10:25:23 +0000] "GET /index.html HTTP/1.1" 200 1043
192.168.1.1 - - [22/Sep/2024:10:25:24 +0000] "POST /login.php HTTP/1.1" 302 511
10.0.0.5 - - [22/Sep/2024:10:25:25 +0000] "GET /images/logo.png HTTP/1.1" 200 2040"""

# Write the sample log to a file for testing
with open('sample_log.txt', 'w') as f:
    f.write(log_file)

# Parse the log file and print the parsed entries
log_entries = parse_log_file('sample_log.txt')
for entry in log_entries:
    print(entry)