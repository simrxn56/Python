import csv
import datetime

class Library:
    members = 0

    def __init__(self, name):
        self._name = name
        self._id = Library.members + 1
        Library.members += 1


    def __str__(self):
        return f"Member Name = {self._name}\nMember ID = {self._id}"
    

    @property
    def name(self):
        return self._name
    
    @property
    def id(self):
        return self._id


    def borrow_book(self):
        book_name = input("What book do you want to borrow? ")
        author_name = input("What is it's author's name? ")
        with open("C:/Users/LENOVO/OneDrive/Desktop/PYTHON/OOP/library/book.csv", "r", newline="") as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            fieldnames = reader.fieldnames

        for row in rows:
            if row["title"] == book_name and row["author"] == author_name:
                if row["status"] == "Available":
                    print(f"{row['title']} by {row['author']} has been issued to you.")
                    row["status"] = "Borrowed"
                else:
                    print("Book is not available.")

        with open("C:/Users/LENOVO/OneDrive/Desktop/PYTHON/OOP/library/book.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

        with open("C:/Users/LENOVO/OneDrive/Desktop/PYTHON/OOP/library/entry.csv", "r", newline="") as file:
            reader = csv.DictReader(file)
            entries = list(reader)
            fieldnamese = reader.fieldnames

            today_date = datetime.date.today()
            return_date = today_date + datetime.timedelta(days=14)

            for row in rows:
                 if row["title"] == book_name and row["author"] == author_name:
                    new_entry = {
                        "type": "Borrowing",
                        "date": today_date,
                        "member id": self._id,
                        "member name": self._name,
                        "book name": book_name,
                        "book id": row['id'],
                        "remarks": "books borrowed"
                    }

        with open("C:/Users/LENOVO/OneDrive/Desktop/PYTHON/OOP/library/entry.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnamese)
            writer.writeheader()
            writer.writerows(entries + [new_entry])


    def return_book(self):
        book_name = input("What book do you want to return ?")
        author_name = input("What is it's author's name? ")
        with open("C:/Users/LENOVO/OneDrive/Desktop/PYTHON/OOP/library/book.csv", "r", newline="") as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            fieldnames = reader.fieldnames

        for row in rows:
            if row["title"] == book_name and row["author"] == author_name:
                if row["status"] == "Borrowed":
                    row["status"] = "Available"

        with open("C:/Users/LENOVO/OneDrive/Desktop/PYTHON/OOP/library/book.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

        with open("C:/Users/LENOVO/OneDrive/Desktop/PYTHON/OOP/library/entry.csv", "r", newline="") as file:
            reader = csv.DictReader(file)
            entries = list(reader)
            fieldnamese = reader.fieldnames

            today_date = datetime.date.today()

            for row in rows:
                 if row["title"] == book_name and row["author"] == author_name:
                    new_entry = {
                        "type": "Returning",
                        "date": today_date,
                        "member id": self._id,
                        "member name": self._name,
                        "book name": book_name,
                        "book id": row['id'],
                        "remarks": "book returned"
                    }

        with open("C:/Users/LENOVO/OneDrive/Desktop/PYTHON/OOP/library/entry.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnamese)
            writer.writeheader()
            writer.writerows(entries + [new_entry])

    def add_books(self):
        noOfBooks = input("How many books do you want to add ?: ")
        for i in range(int(noOfBooks)):
            book_name = input("Please enter book name: ")
            author_name = input("Please enter author name: ")

            with open("C:/Users/LENOVO/OneDrive/Desktop/PYTHON/OOP/library/book.csv", "r", newline="") as file:
                reader = csv.DictReader(file)
                rows = list(reader)
                fieldnames = reader.fieldnames

            for row in rows:
                if row["title"] == book_name and row["author"] == author_name:
                    print("Book already exists in the library.")
                else:
                    new_row = {"id": int(row["id"]) + 1,"title": book_name, "author": author_name, "status": "Available"}

            with open("C:/Users/LENOVO/OneDrive/Desktop/PYTHON/OOP/library/book.csv", "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(rows + [new_row])

            with open("C:/Users/LENOVO/OneDrive/Desktop/PYTHON/OOP/library/entry.csv", "r", newline="") as file:
                reader = csv.DictReader(file)
                entries = list(reader)
                fieldnamese = reader.fieldnames

                today_date = datetime.date.today()

                new_entry = {
                    "type": "Adding",
                    "date": today_date,
                    "member id": self._id,
                    "member name": self._name,
                    "book name": book_name,
                    "book id": new_row['id'],
                    "remarks": "books added"
                }

            with open("C:/Users/LENOVO/OneDrive/Desktop/PYTHON/OOP/library/entry.csv", "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=fieldnamese)
                writer.writeheader()
                writer.writerows(entries + [new_entry])
        print("Books added in the library.")

members = []

def adding_member():
    name = input("Please enter your name: ")
    member = Library(name)
    members.append(member)
    return member

def borrowing_books():
    books = int(input("How many books do you want to borrow? "))
    name = input("Enter your name: ")
    for i in members:
        if i.name == name:
            for n in range(books):
                i.borrow_book()

def returning_books():
    books = int(input("How many books do you want to return? "))
    name = input("Enter your name: ")
    for i in members:
        if i.name == name:
            for n in range(books):
                i.return_book()

def adding_books():
    name = input("Enter your name: ")
    for i in members:
        if i.name == name:
            i.add_books()


def main():
    print("Welcome to the Library")
    while True:
        try:
            options = ["A. Registration in library", "B. Borrow books", "C. Return books", "D. Add books", "E. Exit"]
            print("How can we help you ?")
            for option in options:
                print(option)
            response = input("Enter your choice (like A): ").upper()
            match response:
                case "A":
                    print(print(adding_member()))
                    print("Welcome as a new member in the library.")
                case "B":
                    borrowing_books()
                    print("Happy reading.")
                case "C":
                    returning_books()
                    print("Hope you enjoyed your reading.")
                case "D":
                    adding_books()
                    print("Thanks for adding new books.")
                case "E":
                    print("Thanks for visiting the library.")
                    break
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()