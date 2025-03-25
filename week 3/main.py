Prize = input("Enter prize of item: ")
Discount_percent = input("Enter the discount%: ")

def discount(Prize, Discount_percent):
    return Prize / (1 + (Discount_percent / 100))

try:
    Prize = float(Prize)
    Discount_percent = float(Discount_percent)
    if Discount_percent >= 20:
        print(discount(Prize, Discount_percent))
    else:
        print(Prize)
except ValueError:
    print("Please enter a valid parameter for the fields above")
