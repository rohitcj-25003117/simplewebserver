from http.server import HTTPServer, BaseHTTPRequestHandler

content = '''
<!doctype html>
<html>
    <head>
        <title>Sample
        </title>
    </head>
    <body>
        <font color="black" face="Lucida Handwriting" size="100">
            <h1 align="center"> <b> List of protocol in TCP/IP Model</b></h1>
        </font>
        <font color="green">
        <h2>
            Application Layer - HTTP, FTP, DNS, Telnet & SSH <br>
            Transport Layer - TCP & UDP <br>
            Network Layer - IPV4/IPV6 <br>
        </h2>
        </font>
    </body>
</html>
'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()