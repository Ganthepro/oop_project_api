from pydantic import BaseModel

class EditDisplayNameModel(BaseModel):
    display_name: str

class EditPicUrlModel(BaseModel):
    url: str