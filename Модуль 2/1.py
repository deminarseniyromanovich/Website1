class Book:
    PI = 3.1415



    def __init__(self, id):
        self.id = id

    def get_id(self):
        return self.id
    
    def get_PI():
        return Book.PI
    
print(Book.get_PI())
