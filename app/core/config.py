from dataclasses import dataclass

@dataclass
class Settings:
    DATABASE_URL : str
    CORS_allow_origins : list[str]

def get_settings()->Settings:
    return Settings(
        DATABASE_URL = "postgresql+psycopg://postgres:admin@localhost:5432/postgres",
        CORS_allow_origins =["http://localhost:3000"]
    )