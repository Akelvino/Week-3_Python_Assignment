def calculate_discount(price,discount_percent):
    #if dicount is 20% or higher applly the discount else return the price
    if(discount_percent >= 20):
        disc = (100 - discount_percent)/100
        return f'Tota amount to be paid is Ksh {price * disc},'
    else:
        return f'Total amount to be paid {price}'
    
price = int(input("What is the price \n"))
discount_percent=int(input("What is your discount \n"))

print(calculate_discount(price,discount_percent))
