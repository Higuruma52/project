from typing import TYPE_CHECKING

from sqlalchemy import String, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.database import Base

if TYPE_CHECKING:
    from app.models.roles import UserModel
    from app.models.roles import TicketModel


class PurchasesModel(Base):
    __tablename__ = "Purchases"
    id: Mapped[int] = mapped_column(primary_key=True)
    price: Mapped[int] = mapped_column(nullable=False)

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    user: Mapped["RoleModel"] = relationship(back_populates="purchases")

    ticket_id: Mapped[int] = mapped_column(ForeignKey("ticket.id"), nullable=False)
    ticket: Mapped["TicketModel"] = relationship(back_populates="purchases")
