from pydantic import BaseModel, Field, Validator
from typing import List
import re


class ConverterInput(BaseModel):
    price: float = Field(gt=0)
    to_currency: List[str]

    @Validator("to_currency")
    def validate_to_currencies(cls, values):
        for currency in values:
            if not re.match("", currency):
                raise ValueError(f"Invalidade currency: {currency}")
        return values

class ConverterOutput(BaseModel):
    message: str
    data: List[str]
