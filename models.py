from typing import Optional, List
from uuid import UUID, uuid4
from pydantic import BaseModel, Field
from enum import Enum


class Gender(str, Enum):
    male = "male"
    female = "female"


class Role(str, Enum):
    manager = "manager"
    barista = "barista"
    cashier = "cashier"


class User(BaseModel):
    id: Optional[UUID] = Field(default_factory=uuid4)
    first_name: str
    last_name: str
    middle_name: Optional[str] = None # Assigned a default value of None
    gender: Gender
    roles: List[Role]
