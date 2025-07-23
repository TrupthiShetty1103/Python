'''write a program to manage users of library by creating user id ,user name , user contact as dtat 
members where add user , serach user , lsit of users are fucntion members based on end user details 
and reuirements create user management system NOTE:to store the data use a dictionary called as user
'''
class User:
    def use(self, user_id, user_name, user_contact):
        self.user_id = user_id
        self.user_name = user_name
        self.user_contact = user_contact
class Library(User):
    dict={}
    def add_user(self):
        self.dict[self.user_id]= {"user_name": self.user_name, "user_contact": self.user_contact}
        return {"user_id": self.user_id, "user_name": self.user_name, "user_contact": self.user_contact}
    def remove_user(self,user_id):
        if user_id in self.dict:
            del self.dict[user_id]
            return "user removed"
        else:
            return "user not found"
    def search_user(self,user_id):
        if user_id in self.dict:
            return {"user_id": user_id, **self.dict[user_id]}
        else:
            return "not found"
    def display_users(self):
        return self.dict
s=Library()
while True:
    print("1.add \n2.remove \n3.search \n4.display \n5.exit")
    c=int(input())
    if c==1:
        user_id=int(input("user_id:"))
        user_name=input("user_name:")
        user_contact=input("user_contact:")
        s.use(user_id,user_name,user_contact)
        print(s.add_user())
        continue
    elif c==2:
        user_id=int(input("user_id:"))
        print(s.remove_user(user_id))
        continue
    elif c==3:
        user_id=int(input("user_id:"))
        print(s.search_user(user_id))
    elif c==4:
        print(s.display_users())
        continue
    elif c==5:
        break
    else:
        print("invalid choice")
    