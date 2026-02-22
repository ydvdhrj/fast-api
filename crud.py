from fastapi import FastAPI
from pydantic import BaseModel

books = [
    {
        'id' : 1,
        'title' : 'The Alchemist',
        'auther' : 'Paulo Coelho',
        'publish_date' : '1988-01-04'
    },
    {
        'id' : 2,
        'title' : 'the god of small things',
        'auther' : 'Arudhati Roy',
        'publish_date' : '1997-01-04'
    },
    {
        'id' : 3,
        'title' : 'book 3',
        'auther' : 'auther3',
        'publish_date' : '2000-01-04'
    },
    {
        'id' : 4,
        'title' : 'book 4',
        'auther' : 'auther 4',
        'publish_date' : '2012-01-04'
    }

]

app = FastAPI()

@app.get("/book")
def get_books():
    return books