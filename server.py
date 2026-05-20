from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


class ConverterHandler(SimpleHTTPRequestHandler):
    extensions_map = {
        **SimpleHTTPRequestHandler.extensions_map,
        ".html": "text/html; charset=utf-8",
        ".js": "text/javascript; charset=utf-8",
        ".css": "text/css; charset=utf-8",
    }

    def translate_path(self, path):
        if path == "/":
            return str(Path.cwd() / "INDEX.HTML")
        return super().translate_path(path)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()


if __name__ == "__main__":
    port = 3000
    server = ThreadingHTTPServer(("localhost", port), ConverterHandler)
    print(f"PDF Image Converter running at http://localhost:{port}")
    server.serve_forever()
