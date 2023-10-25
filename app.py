from typing import List, Optional
from uuid import uuid4
from fastapi import FastAPI
from models import Gender, Role, User

app = FastAPI()

# Database: A list of users
db: List[User] = [
    User(
        id=uuid4(),
        first_name='Sharon',
        last_name='Kandall',
        gender=Gender.female,
        roles=[Role.manager]
    ),
    User(
        id=uuid4(),
        first_name='Raphael',
        last_name='Kingston',
        gender=Gender.male,
        roles=[Role.manager]
    ),
    User(
        id=uuid4(),
        first_name='Jesicca',
        last_name='Trevor',
        gender=Gender.female,
        roles=[Role.barista]
    ),
    User(
        id=uuid4(),
        first_name='Uche',
        last_name='Momodu',
        middle_name='Geniee',
        gender=Gender.male,
        roles=[Role.barista]
    ),
    User(
        id=uuid4(),
        first_name='Dave',
        last_name='Babalola',
        middle_name='James',
        gender=Gender.male,
        roles=[Role.barista]
    ),
    User(
        id=uuid4(),
        first_name='Vincent',
        last_name='Sire',
        gender=Gender.male,
        roles=[Role.barista]
    ),
    User(
        id=uuid4(),
        first_name='Folasade',
        last_name='Oyedele',
        middle_name='Genevieve',
        gender=Gender.female,
        roles=[Role.cashier]
    ),
]


@app.get("/")  # annotation: gives route for a get request
def root():
    return {"Name": "Godswill Umukoro"}


@app.get('/api/v1/users')
async def fetch_users():
    return db
