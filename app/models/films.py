from typing import TYPE_CHECKING

from sqlalchemy import String, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.database import Base

if TYPE_CHECKING:
    from app.models.roles import TicketModel
    from app.models.roles import ReviewModel


class FilmModel(Base):
    __tablename__ = "films"
    id: Mapped[int] = mapped_column(primary_key=True)
    images: Mapped[str] = mapped_column(String(255), nullable=False)
    duration: Mapped[str] = mapped_column(String(20), nullable=False)
    name: Mapped[str] = mapped_column(String(50), nullable=False)

    name: Mapped["TicketModel"] = relationship(back_populates="films")
