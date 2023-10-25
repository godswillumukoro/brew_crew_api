from typing import List, Optional
from uuid import UUID, uuid4
from fastapi import FastAPI
from models import Gender, Role, User

app = FastAPI()

# Database: A list of users
db: List[User] = [
    User(
        id=UUID("3c8ba225-816b-45f3-b73b-0ad99b4d2ed7"),
        first_name='Sharon',
        last_name='Kandall',
        gender=Gender.female,
        roles=[Role.manager]
    ),
    User(
        id=UUID("1e3d86ba-eb83-44fa-80c9-519a8d16a742"),
        first_name='Raphael',
        last_name='Kingston',
        gender=Gender.male,
        roles=[Role.manager]
    ),
    User(
        id=UUID("b69af02c-4b41-46ba-8306-86b7fd5d479d"),
        first_name='Jesicca',
        last_name='Trevor',
        gender=Gender.female,
        roles=[Role.barista]
    ),
    User(
        id=UUID("e9e86dee-38cb-4ea7-b452-a54d9b3cf6cf"),
        first_name='Uche',
        last_name='Momodu',
        middle_name='Geniee',
        gender=Gender.male,
        roles=[Role.barista]
    ),
    User(
        id=UUID("5cc985de-1f9f-4f7f-ab80-d211beee8ab9"),
        first_name='Dave',
        last_name='Babalola',
        middle_name='James',
        gender=Gender.male,
        roles=[Role.barista]
    ),
    User(
        id=UUID("b4dc5b46-9187-45f8-b3dc-87535f159c0f"),
        first_name='Vincent',
        last_name='Sire',
        gender=Gender.male,
        roles=[Role.barista]
    ),
    User(
        id=UUID("730e0b20-cd20-40ac-a3b6-9beb982ca65d"),
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
