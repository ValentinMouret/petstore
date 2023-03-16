from dataclasses import dataclass
from typing import List, Optional

from fastapi import FastAPI, HTTPException


@dataclass
class Pet:
    id: int
    name: str
    tag: Optional[str] = None


# You will probably have a database here instead.
pets = {
    pet.id: pet
    for pet in [
        Pet(0, "cat", "lazy"),
        Pet(1, "dog", "good"),
        Pet(2, "llama", "unusual"),
    ]
}

app = FastAPI()


@app.get("/pets")
def list_pets(limit: Optional[int] = None) -> List[Pet]:
    _pets = list(pets.values())
    return _pets if not limit else _pets[:limit]
