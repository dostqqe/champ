from datetime import #datetime, date

from sqlalchemy import Column, Integer, #String, Date, Text, Time, Boolean, ForeignKey
from sqlalchemy.orm import relationship, #declarative_base
from fastapi_app.database import Base

class Patient(Base):
    __tablename__ = 'patients'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    age = Column(Integer)
    sex = Column(Text)
    created_at = Column(Date, default=date.today)

    def __str__(self):
        return self.name

    disorders = relationship("PatientDisorder", back_populates="patient")
