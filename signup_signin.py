l=[]
def signup():
  email=input("Enter a email : ")
  password=input("password : ")  
  if email.endswith("@gmail.com"):
    a={
        "e":email,
        "p":password,
        }
    l.append(a)
  else:
        print("Enter a valid gmail") 

def login():
    email1=input("plz Enter your email : ")
    password1=input("password : ")
    b={
        "e":email1,
        "p":password1,
        }
    for i in l:
      if i["e"] == email1 and i["p"] == password1:
        print("You successfully login in") 
        p=int(input("Select an option\n1.logout\n2.exit\n"))
        if p=='1':
          print("logout successfully")
          
        else:
          break
      else:
        print("Incorrect email or password. Please try again.")
print("create an account -->>")
signup()
while 1:
  z=input("Select an option\n1.login\n2.signup\n3.exit\n")
  if z=='1':    
    login()
    continue
  elif z=='2':
    signup()
  elif z=='3':
    print("Exit")
    break
