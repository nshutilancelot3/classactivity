import os
import json
from datetime import datetime

class BaseClass:
    def __init__(self, id):
        self.id = id
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def filename(self):
        return f"{self.id}.json"

    def save(self):
        data = self.__dict__
        with open(self.filename(), 'w') as f:
            json.dump(data, f, default=str, indent=2)

    def load_or_save(self):
        if os.path.exists(self.filename()):
            with open(self.filename(), 'r') as f:
                self.__dict__.update(json.load(f))
        else:
            self.save()

    def touch(self):
        self.updated_at = datetime.now()
        self.save()


class Book(BaseClass):
    def __init__(self, id, title, author, year, genre):
        super().__init__(id)
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.available = True
        self.load_or_save()


class User(BaseClass):
    def __init__(self, id, name):
        super().__init__(id)
        self.name = name
        self.load_or_save()

    def borrow_book(self, book):
        if book.available:
            book.available = False
            book.touch()
        else:
            print(f"'{book.title}' is already borrowed")


Book1 = Book("b1", "Berserk", "Kentaro Miura", 1989, "Dark Fantasy")
Mamadou = User("u1", "Mamadou")
Mamadou.borrow_book(Book1)
print(Book1.available)
Mamadou.borrow_book(Book1)
print(Book1.available)
Mamadou.save()