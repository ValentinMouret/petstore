# Petstore

This is an implementation of the [Petstore API](https://github.com/OAI/OpenAPI-Specification/blob/main/examples/v2.0/yaml/petstore.yaml) using [FastAPI](https://fastapi.tiangolo.com).

## Quickstart
### Installation
You need Python and [Poetry](https://python-poetry.com) installed, then run: `poetry install`.

You will also need prism: `npm ci`

### Run
`poetry run uvicorn petstore.server:app --reload`

## Prism
We use the Prism proxy to develop our API server.
First, have the API server running in a terminal, and open a new one for the proxy.

Have it running with: `npx prism proxy spec.yaml http://127.0.0.1:8000 --errors`
