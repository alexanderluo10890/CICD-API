# CI/CD Mini FastAPI

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?logo=fastapi)
![Docker](https://img.shields.io/badge/Docker-GHCR-2496ED?logo=docker)
![CI](https://github.com/alexanderluo10890/CICD-API/actions/workflows/ci.yml/badge.svg)
![CD](https://github.com/alexanderluo10890/CICD-API/actions/workflows/cd.yml/badge.svg)

A minimal FastAPI service that demonstrates a production-style CI/CD pipeline using **GitHub Actions** and **GitHub Container Registry (GHCR)**. The app itself is intentionally simple — the focus is the automation around it.

---

## Tech Stack

- **FastAPI** — API framework
- **uvicorn** — ASGI server
- **pytest + httpx** — testing
- **ruff** — linting
- **Docker** — containerization
- **GitHub Actions** — CI/CD automation
- **GHCR** — container image registry

---

## Features

- `GET /health` — liveness check, returns `{ "status": "ok" }`
- `GET /echo/{msg}` — echoes back any message

---

## CI/CD Pipeline

### CI — runs on every PR and push to `main`

| Step | Tool | What it does |
|------|------|-------------|
| Lint | `ruff` | Enforces code style (E/F/I rules) |
| Test | `pytest` | Runs unit tests against the API |
| Build check | `docker build` | Validates the image builds cleanly |

### CD — runs only on merge to `main`

Builds the Docker image and pushes two tags to GHCR:

| Tag | Purpose |
|-----|---------|
| `latest` | Always points to the newest build |
| `<commit-sha>` | Immutable tag for each release |

---

## Run Locally

**With Python:**
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

**With Docker:**
```bash
docker build -t cicd-mini-api .
docker run -p 8000:8000 cicd-mini-api
```

**Pull the published image from GHCR:**
```bash
docker pull ghcr.io/alexanderluo10890/cicd-mini-fastapi:latest
docker run -p 8000:8000 ghcr.io/alexanderluo10890/cicd-mini-fastapi:latest
```

Visit `http://localhost:8000/docs` for the auto-generated Swagger UI.

---

## Run Tests

```bash
pytest -q
```

---

## What I Learned

- How to split CI and CD into separate workflows so a failed publish never blocks a passing test run
- Using commit SHAs as immutable image tags so every merge is independently deployable
- Docker build smoke tests in CI catch broken `Dockerfile`s before they reach the registry
- Keeping the app simple makes it easy to focus on the pipeline itself rather than application logic
