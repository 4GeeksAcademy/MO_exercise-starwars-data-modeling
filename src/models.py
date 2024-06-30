# import os
# import sys
# from sqlalchemy import Column, ForeignKey, Integer, String
# from sqlalchemy.orm import relationship, declarative_base
# from sqlalchemy import create_engine
# from eralchemy2 import render_er

# Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

# ## Draw from SQLAlchemy base
# render_er(Base, 'diagram.png')
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime # type: ignore
from sqlalchemy.orm import relationship, declarative_base # type: ignore
from sqlalchemy import create_engine # type: ignore
from eralchemy2 import render_er # type: ignore

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(50), nullable=False, unique=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(50))
    password = Column(String(16), nullable=False)

class Posts(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    description = Column(String(500))
    body = Column(String(2500), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    users = relationship(Users)

    def to_dict(self):
        return {}
    
class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    homeworld_id = Column(Integer, ForeignKey('planets.id'))
    homeworld = relationship('Planets')

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    director = Column(String(150), nullable=False)
    year = Column(DateTime)


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')