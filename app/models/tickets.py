from typing import TYPE_CHECKING

from sqlalchemy import String, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.database import Base

if TYPE_CHECKING:
    from app.models.roles import FilmModel


class TicketModel(Base):
    __tablename__ = "tickets"
    id: Mapped[int] = mapped_column(primary_key=True)
    price: Mapped[str] = mapped_column(nullable=False)

    film_name: Mapped[str] = mapped_column(ForeignKey("film.name"), String(50), nullable=False)
    film: Mapped["FilmModel"] = relationship(back_populates="tickets")
