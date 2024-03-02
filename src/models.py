import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    favorites = relationship("FavoriteItem", back_populates="user")
    characters = relationship("Character", back_populates="user")
    planets = relationship("Planet", back_populates="user")

class FavoriteItem(Base):
    __tablename__ = 'favorite_item'
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="favorites")
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title
        }

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    species = Column(String(250))
    gender = Column(String(50))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship("Planet", back_populates="characters")
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="characters")
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'species': self.species,
            'gender': self.gender
        }

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    population = Column(Integer)
    climate = Column(String(250))
    characters = relationship("Character", back_populates="planet")
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="planets")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'species': self.species,
            'planet_id': self.planet_id,
            'climate': self.climate,
            'population': self.population

        }



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
