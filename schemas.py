from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class ContactMessage(BaseModel):
    name: str = Field(..., min_length=2, description="Sender name")
    email: EmailStr
    subject: Optional[str] = Field(None, max_length=120)
    message: str = Field(..., min_length=10, max_length=5000)
