# api_server.py 完整代码
from http.server import BaseHTTPRequestHandler, HTTPServer

# 定义请求处理器
class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 设置响应状态码
        self.send_response(200)
        # 设置响应头
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        # 响应内容（包含版本号，后续可修改）
        self.wfile.write(b'{"version": "2.0 - Docker Edition"}')

# 启动服务
if __name__ == '__main__':
    server_address = ('', 8080)  # 监听8080端口
    httpd = HTTPServer(server_address, MyHandler)
    print('Server running on port 8080...')
    httpd.serve_forever()