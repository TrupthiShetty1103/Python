'''program tosimulate library management system with help of class and object ,basic datatype dictionary 
design and imolement library management system the systems should allow librarians and users to manage books and respective records
a)create a function asadd book
b)remove book
c)search book
d)display list of books present in library
(bookid,bookname,authorname)'''
class Library:
    dict={}
    def book(self,book_id,book_name,author_name):
        self.book_id=book_id
        self.book_name=book_name
        self.author_name=author_name
    def add_book(self):
        self.dict[self.book_id]= {"book_name": self.book_name, "author_name": self.author_name}
        return {"book_id": self.book_id, "book_name": self.book_name, "author_name": self.author_name}
    def remove_book(self,book_id):
        if book_id in self.dict:
            del self.dict[book_id]
            return "book removed"
        else:
            return"book not found"
    def search_book(self,book_id):
        if book_id in self.dict:
            return {"book_id": book_id, **self.dict[book_id]}
        else:
            return "not found"
    def display_books(self):
        return self.dict
s=Library()
while True:
    print("1.add \n2.remove \n3.search \n4.display \n5.exit")
    c=int(input())
    if c==1:
        book_id=int(input("book_id:"))
        book_name=input("book_name:")
        author_name=input("author_name:")
        s.book(book_id,book_name,author_name)
        print(s.add_book())
        continue
    elif c==2:
        book_id=int(input("book_id:"))
        print(s.remove_book(book_id))
        continue
    elif c==3:
        book_id=int(input("book_id:"))
        print(s.search_book(book_id))
    elif c==4:
        print(s.display_books())
        continue
    elif c==5:
        break
    else:
        print("invalid choice")
    