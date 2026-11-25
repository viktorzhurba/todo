
uv sync --all-extras --all-groups

docker run -e POSTGRES_PASSWORD=admin -p 5432:5432 -d postgres

uv run uvicorn app.main:app --port 8080 --reload

API на http://127.0.0.1:8080.


json
[
  {
    "id": " ",
    "title": " ",
    "completed": false
  },
]
