import os
import sys

from sqlalchemy import Column, ForeignKey, Integer, String, Text, Float, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String, nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String, nullable=False)

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    image_url = Column(String)
    description = Column(Text)
    gender = Column(String, nullable=False)
    height = Column(Integer)
    hair_color = Column(String)
    eye_color = Column(String)
    name = Column(String)
    birth_year = Column(Integer)
    Character_id = Column(Integer, ForeignKey('character.id'))
    Character = relationship('Favorite')

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    image_url = Column(String)
    description = Column(Text)
    climate = Column(String)
    population = Column(Integer)
    terrain = Column(String)
    diameter = Column(Float)
    surface_water = Column(Integer)
    orbital_period = Column(Integer)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    Planet = relationship('Favorite')

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    image_url = Column(String)
    description = Column(Text)
    name = Column(String)
    model_name = Column(String)
    manufacturer = Column(String)
    price = Column(Integer)
    Vehicle_id = Column(Integer, ForeignKey('planet.id'))
    Vehicle = relationship('Favorite' )

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    body = Column(Text)
    user_id = Column(Integer)
    created_at = Column(DateTime)
    modified_at = Column(DateTime)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship('User', 'Comment')

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment = Column(Text)
    created_at = Column(DateTime)
    user_id = Column(Integer)
    post_id = Column(Integer, ForeignKey('post.id'))
    comment = relationship('User', 'Post')

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    post_id = Column(Integer, ForeignKey('post.id'))
    Character_id = Column(Integer, ForeignKey('character.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    Vehicle_id = Column(Integer, ForeignKey('vehicle.id'))
    favorite = relationship('User', 'Post', 'Character', 'Vehicle', 'Planet')

def to_dict(self):
    return {}


try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem generating the diagram")
    raise e

