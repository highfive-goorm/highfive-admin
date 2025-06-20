# admin/app/database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(usecwd=True))

PG_HOST = os.getenv("PG_HOST")
PG_PORT = os.getenv("PG_PORT",5432)
PG_USER =os.getenv("PG_USER")
PG_PASSWORD = os.getenv("PG_PASSWORD")
PG_NAME = os.getenv("PG_NAME")

DATABASE_URL = f"postgresql+psycopg2://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_NAME}"

engine = create_engine(
    DATABASE_URL       # 유휴 커넥션이 죽어있으면 자동 재커넥트
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

