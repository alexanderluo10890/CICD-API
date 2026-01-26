# CI/CD Mini FastAPI (GitHub Actions + Docker + GHCR)

Small FastAPI service used to demonstrate a real CI/CD pipeline.

## What this repo shows
- **CI (GitHub Actions):** runs on PRs and pushes to `main`
  - Lint with `ruff`
  - Unit tests with `pytest`
  - Docker build validation
- **CD:** on merges to `main`, builds a Docker image and publishes to **GitHub Container Registry (GHCR)**
  - Tags: `latest` and the commit SHA (immutable release tag)

## Endpoints
- `GET /health` → `{ "status": "ok" }`
- `GET /echo/{msg}` → `{ "echo": "..." }`

## Run locally
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```
