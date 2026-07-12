
from sqlalchemy import Text, String
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from app.models.database import db




class Info(db.Model):
    __tablename__ = 'infos'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    text: Mapped[str] = mapped_column(Text, nullable=False)
    date: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    def __repr__(self) -> str:
        return '<Info {self.title}>'