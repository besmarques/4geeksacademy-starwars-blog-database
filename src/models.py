import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

#class Person(Base):
#    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
#    id = Column(Integer, primary_key=True)
#    name = Column(String(250), nullable=False)

#class Address(Base):
#    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
#    id = Column(Integer, primary_key=True)
#    street_name = Column(String(250))
#    street_number = Column(String(250))
#    post_code = Column(String(250), nullable=False)
#    person_id = Column(Integer, ForeignKey('person.id'))
#    person = relationship(Person)

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    image = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    manufacturer = Column(String(250), nullable=False)
    vehicle_class = Column(String(250), nullable=False)
    cost = Column(Integer, nullable=False)
    speed = Column(Integer, nullable=False)
    length = Column(Integer, nullable=False)
    cargo_capacity = Column(String(250), nullable=False)
    crew = Column(Integer, nullable=False)
    passengers = Column(Integer, nullable=False)
    consumables = Column(Integer, nullable=False)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    image = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    diameter = Column(String(250), nullable=False)
    rotation = Column(String(250), nullable=False)
    orbital_period = Column(String(250), nullable=False)
    gravity = Column(String(250), nullable=False)
    population = Column(Integer, nullable=False)
    climate = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    surface_water = Column(Integer, nullable=False)

class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    image = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    birth_year = Column(String(250), nullable=False)
    height = Column(Integer, nullable=False)
    weight = Column(Integer, nullable=False)
    gender = Column(String(250), nullable=False)
    hair_color = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    vehicles = Column(Integer, ForeignKey('vehicles.id'))
    vehicles = relationship(Vehicles)
    homeworld = Column(Integer, ForeignKey('planets.id'))
    planets = relationship(Planets)
    
   
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    character_post_id = Column(Integer, ForeignKey('characters.id'))
    characters = relationship(Character)
    vehicles_post_id = Column(Integer, ForeignKey('vehicles.id'))
    vehicles = relationship(Vehicles)
    planets_post_id = Column(Integer, ForeignKey('planets.id'))
    planets = relationship(Planets)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')