from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy import Table

from .database import Base


# winner_game = Table("user_game", 
#                   Column("user_id", Integer, ForeignKey("user.id")),
#                   Column("game_id", Integer, ForeignKey("game.id"))
# )

# loser_game = Table("user_game", 
#                   Column("user_id", Integer, ForeignKey("user.id")),
#                   Column("game_id", Integer, ForeignKey("game.id"))
# )

class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String(255),index=True)
    # won_games = relationship("Game", secondary="winner_game", back_populates="winning_players")
    # lost_games = relationship("Game", secondary="lozer_game", back_populates="losing_players")
    elo = Column(Integer, default=1200)



class Game(Base):
    __tablename__ = "games"
    id = Column(Integer, primary_key=True, index=True)
    player_id = Column(Integer, primary_key=True, index=True)
    # winning_players = relationship("User", secondary="winner_game", back_populates="won_games")
    # losing_players = relationship("User", secondary="loser_game", back_populates="lost_games")
    score_for = Column(Integer)
    score_against = Column(Integer)
    date = Column(String(255))
    description = Column(String(255))
