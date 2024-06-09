from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from . import crud,models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

#Dependency
def get_db():
    db = SessionLocal()
    try : 
        yield db
    finally:
        db.close()


@app.post("/users/",response_model=schemas.User)
def post_user(user:schemas.UserCreate, db:Session=Depends(get_db)):
    db_user = crud.get_user_by_name(db, email=user.name)
    if db_user:
        raise HTTPException(status_code=400, detail="Name already registered")
    return crud.create_user(db=db,user=user)


@app.get("/users/", response_model=list[schemas.User])
def get_users(skip:int=0, limit:int=0, db:Session=Depends(get_db)):
    users = crud.get_users(db,skip=skip,limit=limit)
    return users


@app.get("/users/{user_id}/",response_model=schemas.User)
def get_user(user_id:int, db:Session=Depends(get_db)):
    db_user = crud.get_user(db,user_id =user_id )
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/games/",response_model=schemas.Game)
def post_game_for_user(user_id:int, game:schemas.GameBase, db:Session=Depends(get_db)):
    return crud.create_game_user(db=db,user_id=user_id, game=game)


@app.get("/games/", response_model=list[schemas.Game])
def get_todos(skip:int=0,limit:int=100,db:Session=Depends(get_db)):
    games = crud.get_games(db,skip=skip,limit=limit)
    return games