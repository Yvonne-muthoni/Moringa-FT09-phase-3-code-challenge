from database.connection import get_db_connection
from models.article import Article
class Author:
    def __init__(self, id, name):
        self._id = id
        self._name = name
    @property
    def id(self):
        return self._id
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if not isinstance(value,str):
            raise TypeError("Name must be a string.")
        if len(value)==0:
            raise ValueError("Name must not be empty.")
        if hasattr(self,'_name'):
            raise AttributeError("Name cannot be changed after instantiation.")
        self._name = value
    @classmethod
    def get_authors(cls,cursor):
        cursor.execute("SELECT * FROM authors")
        authors_data = cursor.fetchall()
        return [cls(id=row[0],name=row[1])for row in authors_data]
    def articles(self,cursor):
        cursor.execute("SELECT * FROM articleS WHERE author_id = ?", (self._id,)) 
        articles_data = cursor.fetchall()
        return articles_data   
            