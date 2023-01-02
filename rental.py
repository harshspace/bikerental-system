class bikeShop:
    def __init__(self,stock):
        self.stock=stock
    def displayBike(self):
        print("total bikes",self.stock)
    def rentforBike(self,q):

        if q<=0:
            print("enter the postive value")
        elif q>self.stock:
            print("enter the value(less then stock)")            
        else:
            self.stock=self.stock-q
            print("total price",q*100)
            print("total bikes",self.stock)

while True:
    obj=bikeShop(100)
    uc=int(input('''
 1 display stocks
 2 rent a bike
 3 exit
    '''))            
        
    if uc==1:
        obj.displayBike()
    elif uc==2:
        n=int(input("enter the qty:---")) 
        obj.rentforBike(n)   
    else:
        break    