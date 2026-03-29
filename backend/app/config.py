from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # Database
    database_url: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/clinicalmind"
    sync_database_url: str = "postgresql+psycopg2://postgres:postgres@localhost:5432/clinicalmind"

    # Redis / Celery
    redis_url: str = "redis://localhost:6379/0"
    celery_broker_url: str = "redis://localhost:6379/0"
    celery_result_backend: str = "redis://localhost:6379/1"

    # Anthropic
    anthropic_api_key: str = ""

    # OpenAI (embeddings fallback)
    openai_api_key: str = ""

    # Delivery
    sendgrid_api_key: str = ""
    sendgrid_from_email: str = "alerts@clinicalmind.ai"
    slack_bot_token: str = ""
    slack_default_channel: str = "#clinical-alerts"

    # Auth
    secret_key: str = "changeme"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 1440

    # App
    environment: str = "development"
    log_level: str = "INFO"
    cors_origins: str = "http://localhost:3000"

    # MCP
    mcp_api_key: str = "changeme-mcp-key"

    @property
    def cors_origins_list(self) -> list[str]:
        return [o.strip() for o in self.cors_origins.split(",")]


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
