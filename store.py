def menu():
    print("1. add product")
    print("2. edit product")
    print("3. delete product")
    print("4. search")
    print("5. show all")
    print("6.buy")
    print("7. exit")

product={"1001": "manga", "1002": "dakimakura", "1003": "figure", "1004": "stand", "1005": "novel" }
price={"1001": 150000, "1002": 240000, "1003": 300000, "1004": 50000, "1005": 120000}
count={"1001":20, "1002": 10, "1003": 5, "1004": 13, "1005": 12}

def show():
    print("")
    filetxt=open(".\database.txt", "r")
    mytxt=filetxt.read()
    print(mytxt)
    menu()
    print("")

x=True

while x==True: 
    choice=int(input("please enter a number(1_7): "))
    if choice ==1:
       show()
       code=input("please enter your new code: ")
       product[code]=input("please enter your product name: ")
       price[code]=int(input("please enter your product price: "))
       count[code]=int(input("please enter your product count: "))

    elif choice==2:
        show()
        print("how can i help you?")
        print("edit product name(1)")
        print("edit product price(2)")
        print("edit product count(3)")
        ch=int(input("please enter your choice(1_3): "))
        if ch==1:
            show()
            edit=input("please enter your product code: ")
            del product[edit]
            product[edit]=input("please enter your new product: ")
            print("done!")

        elif ch==2:
            edit=input("please enter : ")
            del product[edit]
            product[edit]=input("please enter your new price: ")
            print("done!")

        elif ch==3:
            edit=input("please enter your product code: ")
            del product[edit]
            product[edit]=input("please enter your new count: ")
            print("done!")
            #ویرایش در فایل 
        print(product)#این لاین حذف شود

    elif choice==3:
        show()
        d=input("please enter your product code: ")
        del product[edit]
        print("done!")
        print(product)#این لاین حذف بشه

    elif choice==4:
        pass
    elif choice==5:
        pass
    elif choice==6:
        pass
    elif choice==7:
        print("Bye")
        x=False