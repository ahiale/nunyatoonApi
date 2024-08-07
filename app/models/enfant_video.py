from sqlalchemy import Table, Column, Integer, String, ForeignKey,Boolean
from database import Base

enfant_video = Table(
    "enfant_video",
    Base.metadata,
    Column("enfant_id", String, ForeignKey("enfants.id"), primary_key=True),
    Column("video_id", String(255), ForeignKey("videos.id"), primary_key=True),
    Column("like", Boolean)
)
