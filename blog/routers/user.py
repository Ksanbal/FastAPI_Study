import re
from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import schemas, models, database, oauth2
from ..hashing import Hash
from ..repository import user_repository as user

router = APIRouter(
    prefix='/user',
    tags=['Users'],
    responses={404: {"description": "Not found"}},
)

get_db = database.get_db

@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request=request, db=db)
    

@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return user.get_one(id=id, db=db)