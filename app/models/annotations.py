import datetime
from sqlalchemy import ForeignKey, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.songs import SongModel


class AnnotationModel(Base):
    __tablename__ = "annotations"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    song_id: Mapped[int] = mapped_column(ForeignKey("songs.id", ondelete="CASCADE"), nullable=False)
    author: Mapped[str] = mapped_column(nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(func.now(), nullable=False)

    song: Mapped["SongModel"] = relationship("SongModel", back_populates="annotations")
