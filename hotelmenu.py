menu={
    
    "pizza":50,
    "pasta":70,
    'burger veg':70,
    "toast sandwhich":60,
    "mango shake":70,
    "chocolate shake":100,
    "cold coffe":80,
    "peri peri fries":60,
    'chicken burger':100,
    
    
}
print("welcome to SATPUTE KITCHEN")
#menu
print("pizza:Rs50\npasta:Rs70\nburger veg: Rs70\ntoast sandwhich; Rs60\nmango shake: Rs70\nchocolate shake: Rs100\ncold coffe: Rs60\nperi peri fries: Rs60\nchicken burger: Rs100")

order_total=0
item_1=input("enter the name of your items you ordered:")
if item_1 in menu:
    order_total+=menu[item_1]
    print(f"your item {item_1} is been added to your order")
else:
    print(f"the ordered item {item_1} is not avalaible,please order something that we can serve you")
    
another_order=input('do you want to add another item?(Yes/No)=')
if another_order=="yes":
    item_2=input("emter the name of second item :")
    if item_2 in menu:
        order_total+=menu[item_2]
        print(f"item{item_2}is been added to your order")
    else:
    
            print(f"ordered item {item_2}is not avaliable")
 
print(f"your total bill is {order_total} ")           
            

