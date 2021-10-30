import calendar
import datetime

    
   
def calander_of_month():
    
        
    y = int(input("Input the Year : "))
    
    m = int(input("Input the Month : "))
    
    print(calendar.month(y, m))
    
def Day_of_Date():

    y = int(input("Input the Year : "))
    
    m = int(input("Input the Month : "))
    
    d = int(input("Input the Date : "))
    
    b = datetime.date(y, m, d) 
    print(b.strftime("%A"))

def List_of_LeapYear():

    list=[]

    c=0
    
    for i in range(2000,3000):
        if ((i % 4 == 0) and (i % 100 != 0) or (i % 400 == 0)):

            c=c+1
            list.append(i)
        
    print("The List of Leap Years are : ",list,"\n")
    print("The no. of Leap Years are : ",c,"\n")



def menu():
    
     
    a=int(input("\nEnter the choice : \n1) Calendar of a Month.\n2) Day for the Date given.\n3) List of the Leap Year(2000-2999).\n4) Exit.\n"))
    if a==1:
        calander_of_month()
    elif a==2:
        Day_of_Date()
    elif a==3:
        List_of_LeapYear()
    elif a==4:
        exit()
    else:
        print("Wrong Choice!!")
        
a=0
while(a!=4):
    
    menu()
        
       
    

