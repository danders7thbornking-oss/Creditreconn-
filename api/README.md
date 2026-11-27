# Creditreconn API

A local FastAPI starter with interactive API documentation and a health endpoint.

## Start on Windows

Run these commands from this directory in PowerShell with Python 3.12 installed.

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m uvicorn main:app --host 127.0.0.1 --port 8000
```

Open [API docs](http://127.0.0.1:8000/docs) or check [service health](http://127.0.0.1:8000/health).

On a Windows machine with a hosts entry mapping `api.creditreconn.home.arpa` to `127.0.0.1`, the [local domain](http://api.creditreconn.home.arpa:8000/docs) serves the same docs. The API listens on loopback only.
