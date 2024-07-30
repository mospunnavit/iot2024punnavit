from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
# from sqlalchemy.orm import relationship

from database import Base

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    descripion = Column(String, index=True)
    synopsis = Column(String, index=True)
    type = Column(String, index=True)
    author = Column(String, index=True)
    year = Column(Integer, index=True)
    is_published = Column(Boolean, index=True)
    picture = Column(String, index=True)
    


class Student(Base):
    __tablename__ = 'Student'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    firstname = Column(String, index=True)
    lastname = Column(String, index=True)
    student_id = Column(String, index=True)
    Gender = Column(String, index=True)
    brithdate = Column(Date, index=True)

class Menu(Base):
    __tablename__ = 'menu'

    menu_id = Column(Integer, primary_key=True, index=True)
    menu_name = Column(String, index=True, unique=True)
    menu_type = Column(String, index=True)
    menu_price = Column(String, index=True)
    menu_picture = Column(String, index=True)

class Order(Base):
    __tablename__ = 'order'

    order_id = Column(Integer, primary_key=True, index=True)
    details = Column(String, index=True)
    status = Column(String, index=True)
    
class Staff(Base):

    staff_id = Column(Integer, primary_key=True, index=True)
    staff_name = Column(String, index=True)
    staff_role = Column(String,index=True)



    

