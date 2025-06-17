import os

class Config:
    # chave usada para flashes, sessão, etc.
    SECRET_KEY = os.getenv("SECRET_KEY", "chave-secreta-padrao")

    # ---------- Conexão MySQL ----------
    DB_USER = os.getenv("DB_USER", "root")
    DB_PW   = os.getenv("DB_PW",   "")          # coloque sua senha ou defina DB_PW
    DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
    DB_PORT = os.getenv("DB_PORT", "3307")
    DB_NAME = os.getenv("DB_NAME", "rota_segura")

    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{DB_USER}:{DB_PW}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        "?charset=utf8mb4"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # ---------- Uploads ----------
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024   # 16 MB por upload
