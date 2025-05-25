from http.server import BaseHTTPRequestHandler
import json
from urllib.parse import urlparse, parse_qs
import os

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

        # Load JSON file from same directory as this script
        with open(os.path.join(os.path.dirname(__file__), "../students.json")) as f:
            marks_db = json.load(f)

        query = parse_qs(urlparse(self.path).query)
        names = query.get("name", [])

        marks = [marks_db.get(name, None) for name in names]
        self.wfile.write(json.dumps({"marks": marks}).encode())
