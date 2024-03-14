class library:
    def __init__(self,name,list):
        self.book=list
        self.name=name
        self.lenddict={}
    def display(self):
        print(f"The Books Present In Our Library:{self.book}")
        for book in self.book:
            print(book)

    def displaydict(self):
        print(self.lenddict)

    def lendbook(self,book,user):
        if book not in self.lenddict.keys():
            self.lenddict.update({book:user})
            self.book.remove(book)
            print("the book have been update,user an take the book now ")
        else:
            print("The book is already in use",{self.lenddict[book]})   
    def returnbook(self, book):
        if book in self.lenddict.keys():
            self.lenddict.pop(book)
            self.book.append(book)
        else:
            print("This book is not present in the lenddict.")
   


if __name__=='__main__':
    krrish = library("Fantasy",["It end with us ","It start with us","Pride and Prejudice","Jane eyres","Slow Train","The Fault in our star"])
while(True):
    print("Welcome to {krrish.name} library")
    print("1: to diplay the Books present in library")
    print("2.To lend the books to user")
    print("3.To return the book")

    user_choice = int(input("Enter you choice"))
    if user_choice == 1:
        krrish.display()
    elif user_choice == 2:
        a = input("enter the name of a book")
        b = input("enter the name of user")
        krrish.lendbook(a,b)
        krrish.displaydict() 
    elif user_choice == 3:
        book = input("enter the name of a book")
        krrish.returnbook(book)
        krrish.display()
        print("The book has been returned")
    else:
        print("you enter the wrong choice")
    
    print("y to continue and N to exit")
    user_choice = input()
    if user_choice == "y":
        continue
    elif user_choice  == "N":
        exit()

    else:
        print("Bye")

