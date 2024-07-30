import string
from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, Depends, Response, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

# Import models
from database import SessionLocal, engine
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
router_v1 = APIRouter(prefix='/api/v1')

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# https://fastapi.tiangolo.com/tutorial/sql-databases/#crud-utils

@router_v1.get('/books')
async def get_books(db: Session = Depends(get_db)):
    return db.query(models.Book).all()

@router_v1.get('/books/{book_id}')
async def get_book(book_id: int, db: Session = Depends(get_db)):
    return db.query(models.Book).filter(models.Book.id == book_id).first()

@router_v1.get('/menus')
async def get_books(db: Session = Depends(get_db)):
    return db.query(models.Menu).all()

@router_v1.post('/order')
async def create_orders(order: dict, response: Response, db: Session = Depends(get_db)):
    # TODO: Add validation
    neworeder = models.Order(details=order['details'], status=order['status'])
    db.add(neworeder)
    db.commit()
    db.refresh(neworeder)
    response.status_code = 201
    return neworeder


@router_v1.get('/menus/{menu_id}')
async def get_book(menu_id: int, db: Session = Depends(get_db)):
    return db.query(models.Menu).filter(models.Menu.menu_id == menu_id).first()

@router_v1.get('/orders')
async def get_books(db: Session = Depends(get_db)):
    return db.query(models.Order).all()

@router_v1.post('/books')
async def create_book(book: dict, response: Response, db: Session = Depends(get_db)):
    # TODO: Add validation
    newbook = models.Book(title=book['title'], author=book['author'], year=book['year'], is_published=book['is_published'],
                           descripion=book['descripion'], type=book['type'], synopsis=book['synopsis'], picture=book['picture'])
    db.add(newbook)
    db.commit()
    db.refresh(newbook)
    response.status_code = 201
    return newbook

@router_v1.post('/books')
async def create_book(book: dict, response: Response, db: Session = Depends(get_db)):
    # TODO: Add validation
    newbook = models.Book(title=book['title'], author=book['author'], year=book['year'], is_published=book['is_published'],
                           descripion=book['descripion'], type=book['type'], synopsis=book['synopsis'], picture=book['picture'])
    db.add(newbook)
    db.commit()
    db.refresh(newbook)
    response.status_code = 201
    return newbook



@router_v1.put('/books/{book_id}')
async def update_book(book_id: int, books: dict, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        return {"detail": "Student not found"}
    for key, value in books.items():
        setattr(book, key, value)
    db.commit()
    db.refresh(book)
    return {"detail": f"StudentID {book_id} updated successfully"}




@router_v1.post('/Students')
async def create_student(student: dict, response: Response, db: Session = Depends(get_db)):
    # TODO: Add validation
    newstudent = models.Student(student_id=student['student_id'], firstname=student['firstname'], lastname=student['lastname'], Gender=student['Gender'], brithdate=student['brithdate'])
    db.add(newstudent)
    db.commit()
    db.refresh(newstudent)
    response.status_code = 201
    return newstudent


@router_v1.get('/Students/{student_id}')
async def get_student(student_id: str, db: Session = Depends(get_db)):
    result = db.query(
        models.Student.student_id, 
        models.Student.firstname, 
        models.Student.lastname,
        models.Student.Gender,
        models.Student.brithdate
    ).filter(
        models.Student.student_id == student_id
    ).first()
    
    if result:
        # Convert the result to a dictionary
        return {
            "student_id": result.student_id,
            "firstname": result.firstname,
            "lastname": result.lastname,
            "Gender": result.Gender,
            "brithdate": result.brithdate
        }
    else:
        return None


@router_v1.put('/Students/{student_id}')
async def update_student(student_id: str, student_data: dict, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.student_id == student_id).first()
    if not student:
        return {"detail": "Student not found"}

    for key, value in student_data.items():
        setattr(student, key, value)

    db.commit()
    db.refresh(student)
    return {"detail": f"StudentID {student_id} updated successfully"}

@router_v1.delete('/Students/{student_id}')
async def delete_student(student_id: str, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.student_id == student_id).first()
    if not student:
        return {"detail": "Student not found"}
    
    db.delete(student)
    db.commit()
    return {"detail": f"StudentID {student_id} deleted successfully"}
# @router_v1.delete('/books/{book_id}')
# async def delete_book(book_id: int, db: Session = Depends(get_db)):
#     pass

app.include_router(router_v1)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)
