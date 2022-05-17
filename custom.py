from http import server
from http.server import HTTPServer , BaseHTTPRequestHandler
import json


host= "192.***.1.255" #replace with your ip
port =9070


class CustomHTTP(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        # self.send_header('Content-type','application/json')
        self.send_header('Content-type','text/html')
        self.end_headers()
        # self.wfile.write(json.dumps({'message':'Hello World'}).encode())
        self.wfile.write(b'<html><body><h1>Hello World</h1></body></html>', "utf-8")



server= HTTPServer((host,9070),CustomHTTP)

print(f"Server started at http://{host}:{port}")
print("Press Ctrl+C to quit")
server.serve_forever()
server.server_close()

print("Server stopped")
