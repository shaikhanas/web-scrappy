import socket

CRLF = "\r\n"

request = [
    "GET /pandas-docs/stable/ HTTP/1.1",
    "Host: https://pandas.pydata.org/",
    "Connection: Close",
    "User-agent: Mozilla/5.0",
    "",
]

# Connect to the server
s = socket.socket()
s.connect(('www.google.com', 80))

# Send an HTTP request
http_packet =  (CRLF.join(request))
s.send(http_packet)
# Get the response (in several parts, if necessary)
response = ''
buffer = s.recv(4096)
while buffer:
    response += buffer
    buffer = s.recv(4096)

# HTTP headers will be separated from the body by an empty line
header_data, _, body = response.partition(CRLF + CRLF)

print (header_data)