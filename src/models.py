import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class LoggedUser(Base):
    __tablename__ = 'logged user'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(Integer, ForeignKey('name.id'))
    user = relationship("User", back_populates="logged_users")
    favorites = relationship("FavoriteItem", back_populates="logged_user")
    characters = relationship("Character", back_populates="logged_user")
    planets = relationship("Planet", back_populates="logged_user")



class FavoriteItem(Base):
    __tablename__ = 'favorite_item'
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    logged_user_id = Column(Integer, ForeignKey('logged_user.id'))
    logged_user = relationship("LoggedUser", back_populates="favorites")


class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    species = Column(String(250))
    gender = Column(String(50))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship("Planet", back_populates="characters")
    logged_user_id = Column(Integer, ForeignKey('logged_user.id'))
    logged_user = relationship("LoggedUser", back_populates="character")

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    population = Column(Integer)
    climate = Column(String(250))
    characters = relationship("Character", back_populates="planet")
    logged_user_id = Column(Integer, ForeignKey('logged_user.id'))
    logged_user = relationship("LoggedUser", back_populates="Planet")

    def to_dict(self):
        return {}



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
