from sqlalchemy import Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base
from typing import List, TYPE_CHECKING
if TYPE_CHECKING:
    from app.models.annotations import AnnotationModel


class SongModel(Base):
    __tablename__ = "songs"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(nullable=False)
    artist: Mapped[str] = mapped_column(nullable=False)
    album: Mapped[str] = mapped_column(nullable=True)
    lyrics: Mapped[str] = mapped_column(Text, nullable=False)

    annotations: Mapped[List["AnnotationModel"]] = relationship(
        "AnnotationModel", back_populates="song", cascade="all, delete-orphan"
    )
