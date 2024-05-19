class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def get_book_info(self):
        return f"Title: {self.title}, Author: {self.author}, Price: {self.price}."

def get_total_price(list_of_books):
    total_price_list_of_books = 0
    for book in list_of_books:
        total_price_list_of_books += book.price

    return total_price_list_of_books

description = "This is a module named bookstore."
    