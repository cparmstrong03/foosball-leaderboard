from pydantic import BaseModel

class GameBase(BaseModel):
    player_id: int
    score_for: int
    score_against: int
    description : str | None = None

# class GameCreate(GameBase):
#     pass 

# class Game(GameBase):
#     id : int

#     class Config:
#         orm_model = True


class UserBase(BaseModel):
    name: str

# class UserCreate(UserBase):
#     pass 

# class User(UserBase):
#     id : int
#     elo : int

#     class Config:
#         orm_model = True