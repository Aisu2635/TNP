#Shopping List
#1. Add item
#2. Remove item
#3. View item
#4. Exit

msg1="TCET gameshop"
print(msg1.center(50,"*"))

l=[]
while(True):
    print("1. Add item")
    print("2. Remove item")
    print("3. View item")
    print("4. Exit")
    ch=int(input("enter your choice: "))
    if ch==1:
        while(True):
            dict={1:"Valorant",2:"CSGO",3:"GTA5",4:"PUBG",5:"Fortnite",6:"Minecraft",7:"Among Us",8:"Fall Guys",9:"Apex Legends",10:"COD"}
            for i in dict:
                print(i,"-->",dict[i])
            ch=int(input("enter your choice: "))
            if ch in dict:
                l.append(dict[ch])
                print(dict[ch],"added to cart")
            else:
                print("invalid choice")
            if ch == 0:
                print("Thank you for shopping")
                break
        

    elif ch==2:
        print("**********************************************************")
        print(l)
        rem=input("enter item to remove: ")
        if rem in l:
            l.remove(rem)
            print("item removed")
        else:
            print("item not found")
    elif ch==3:
        print("**********************************************************")
        print(l)
        sl=sorted(set(l))
        for i in sl:
            print(i,"-->",l.count(i))
    elif ch==4:
        break
    else:
        print("invalid choice")

