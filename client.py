import socket

host = 'fast.com'
port = 80

tcp_client_socket = socket(AF_INET, SOCK_STREAM)

s.connect((host, port))

ip, port = s.getsockname()

http_request = 'GET / HTTP/1.1\r\nhost: {}\r\n\r\n'.format(host)
