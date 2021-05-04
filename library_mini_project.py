import datetime
import ast


class Library:

    def __init__(self, listOfBooks, libraryName):
        self.listOfBooks = listOfBooks
        self.libraryName = libraryName

    def addBook(self, bookName):
        self.listOfBooks.append(bookName)
        return f"{bookName} has been added"

    def lendBook(self, bookName, lenderName):

        while bookName != self.listOfBooks:
            if bookName in self.listOfBooks:
                self.listOfBooks.remove(bookName)
                return f"{lenderName} take the book {bookName}"
            else:
                return "Sorry Your requested book is not available..."
                # break

    def returnBook(self, bookName):
        self.listOfBooks.append(bookName)
        return f"{bookName} has been returned by user"


if __name__ == "__main__":
    with open("MyLibrary.txt", "r")as f:
        libraryBooks = f.readline()  # Here libraryBooks is string of list format

    # it will convert string of list format to List format
    libraryBookList = ast.literal_eval(libraryBooks)
    ap = Library(libraryBookList, "MyLibrary")
    while True:
        try:
            choice = '''*********Welcome to ap's Library*********\n1.AddBook\n2.LendBook\n3.ListOfBooks\n4.ReturnBook\n5.Exit '''
            print("=========================================")
            print(choice)
            print("=========================================")
            user_choice = int(input("Enter Your Choice: "))
            if user_choice == 1:
                book = input("Enter your book Name: ")
                print(ap.addBook(book))
                continue

            if user_choice == 2:
                book = input("Enter book name: ")
                user_name = input("Enter Your name: ")
                print(ap.lendBook(book, user_name))
                time = datetime.datetime.now()
                with open("logOfLibrary.txt", "a")as f:
                    f.write(
                        f"* Lender Name:{user_name}\n Book Name: {book}\n Lending Time: {time}")
                    f.write("\n")

                continue

            if user_choice == 3:
                print(ap.listOfBooks)
                continue

            if user_choice == 4:
                book = input("Enter book Name: ")
                print(ap.returnBook(book))
                time = datetime.datetime.now()
                with open("logOfLibrary.txt", "a")as f:
                    f.write(
                        f"* Book Name: {book}\n Returned Time: {time}")
                    f.write("\n")
                continue
            if user_choice == 5:
                print("Thank you for using our service...")
                libraryBooks = ap.listOfBooks
                with open("MyLibrary.txt", "w") as f:
                    f.write(f"{libraryBooks}")
                    time = datetime.datetime.now()
                    f.write(f"\n Last upadated time:{time}")
                break
            else:
                print("Invalid Input")
        except Exception as e:
            print(e)
