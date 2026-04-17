#!/usr/bin/env python3
"""Servidor HTTP estático puerto 8081 (misma carpeta que este script)."""

import http.server
import os
import socketserver
from pathlib import Path

PORT = 8081

if __name__ == "__main__":
    os.chdir(Path(__file__).resolve().parent)

    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print(f"Servidor en http://127.0.0.1:{PORT}/")
        print(f"Abrí index.html o http://127.0.0.1:{PORT}/index.html")
        print("Ctrl+C para detener.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServidor detenido.")
