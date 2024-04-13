import tkinter as tk
from books import Book
from members import Member

# Mock classes for demonstration purposes
class Member:
    members = {
        1: {"membership_id": 1, "surname": "Doe", "name": "John", "gender": "Male", "address": "123 Main St", "phone": "123-456-7890", "email": "john@example.com", "birthday": "01/01/1990", "age": 30, "job": "Engineer", "membership_status": True},
        2: {"membership_id": 2, "surname": "Smith", "name": "Alice", "gender": "Female", "address": "456 Elm St", "phone": "987-654-3210", "email": "alice@example.com", "birthday": "02/02/1980", "age": 40, "job": "Teacher", "membership_status": False},
    }

class Book:
    books = {
        1: {"title": "Book 1"},
        2: {"title": "Book 2"},
        3: {"title": "Book 3"}
    }

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Library Management System")

        # Menu Bar
        menubar = tk.Menu(self)

        # Members Menu
        members_menu = tk.Menu(menubar, tearoff=0)
        members_menu.add_command(label='List of members', command=self.members_list)
        menubar.add_cascade(label='Members', menu=members_menu)

        # Help Menu
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label='About...', command=self.help_menu)
        menubar.add_cascade(label='Help', menu=help_menu)

        self.config(menu=menubar)

        # List Box with Scrollbar
        scrollbar = tk.Scrollbar(self)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.list_widget = tk.Listbox(self, yscrollcommand=scrollbar.set)
        self.list_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar.config(command=self.list_widget.yview)

        self.book_list()

    def members_list(self):
        """Prints each member from the Member.members dictionary with their information"""
        for member_info in Member.members.values():
            print(f'Αρ. Μητρώου Μέλους: {member_info["membership_id"]}\n'
                  f'Όνομ/πώνυμο: {member_info["surname"]} {member_info["name"]}\n'
                  f'Φύλο: {member_info["gender"]}\n'
                  f'Διεύθυνση: {member_info["address"]}\n'
                  f'Τηλέφωνο: {member_info["phone"]}\n'
                  f'E-mail: {member_info["email"]}\n'
                  f'Ημερ/νία γέννησης: {member_info["birthday"]}\n'
                  f'Ηλικία: {member_info["age"]}\n'
                  f'Επάγγελμα: {member_info["job"]}\n'
                  f'Κατάσταση συνδρομής: {"Ενεργή" if member_info["membership_status"] else "Ανενεργή"}\n')

    def book_list(self):
        """Populates the list widget with the titles of the books"""
        for book in Book.books.values():
            self.list_widget.insert(tk.END, book['title'])

    def help_menu(self):
        print('Help Instructions...')

if __name__ == "__main__":
    window = MainWindow()
    window.mainloop()
