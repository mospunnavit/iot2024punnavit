from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
# from sqlalchemy.orm import relationship

from database import Base

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    year = Column(Integer, index=True)
    is_published = Column(Boolean, index=True)


class Student(Base):
    __tablename__ = 'Student'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    firstname = Column(String, index=True)
    lastname = Column(String, index=True)
    student_id = Column(String, index=True)
    Gender = Column(String, index=True)
    brithdate = Column(Date, index=True)





