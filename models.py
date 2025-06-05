from pydantic import BaseModel
from typing import List, Optional

class StoryRequest(BaseModel):
    type: str
    tone: str
    genre: str
    length: int
    title: Optional[str] = None
    characters: Optional[List[str]] = []
