print("WELCOME TO THE AMANDO SHOPPING SITE\n 1. Add a product to the cart.\n 2. Search for a product. \n 3. Delete a product from the cart. \n 4. Display the contents of the cart. \n 5. Purchase items. \n 6. Quit")
x=int(input("Enter Option:"))

shoppingCART={}

while(x!=6):   
    if(x==1):
        print("Add a product to your cart.")
        a=input("Enter your product & brand name:")
        b=int(input("Enter the price:"))
        shoppingCART.update({a:b})
        if len(shoppingCART)>=5:
            print("Cart is full.")
    
    elif x==2:
        s=input("2. Search for a product:")
        if s in shoppingCART:
            print(s,"==",shoppingCART[s])
        else:
            print("No product exists with this name.")
        
    elif x==3:
        d=input("Delete a product from the cart:")
        if  d in shoppingCART:
            shoppingCART.pop(d)
        else:
            print("not found")
        
    elif x==4:
        print("Display the contents of the cart:")
    
    
    elif x==5:
        print("Purchase items:")
        total=sum(['b'] for price in shoppingCART)
        Con=input("Complete purchase (Y/N)?")
        if (Con=="Y"):
            print("Thank You For Your Business.")
        elif (Con=="N"):\
            print("Please continue shopping.")
        else:
            print("Please answer either Y or N.")
            
    elif x==6:
        print("Quit")

else:
    ("Invalid option: Please enter between 1 & 6.")


