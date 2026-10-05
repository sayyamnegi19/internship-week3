class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.issued = False


class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        self.books[book.book_id] = book
        print(f"Book added: {book.title}")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed = self.books.pop(book_id)
            print(f"Book removed: {removed.title}")
        else:
            print("Book not found")

    def issue_book(self, book_id):
        if book_id in self.books:
            book = self.books[book_id]
            if book.issued:
                print(f"Book '{book.title}' is already issued")
            else:
                book.issued = True
                print(f"Book issued: {book.title}")
        else:
            print("Book not found")

    def return_book(self, book_id):
        if book_id in self.books:
            book = self.books[book_id]
            if book.issued:
                book.issued = False
                print(f"Book returned: {book.title}")
            else:
                print(f"Book '{book.title}' was not issued")
        else:
            print("Book not found")


if __name__ == "__main__":
    library = Library()

    library.add_book(Book(1, "Python Basics", "John Doe"))
    library.add_book(Book(2, "OOP Concepts", "Jane Smith"))

    library.issue_book(1)
    library.issue_book(1)
    library.return_book(1)

    library.remove_book(2)
    library.remove_book(2)
