#shipping cost calculator
##input package weiht and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))

#Calculate shiping cost
Shipping_cost = Weight * rate

##Display the result
print(f"Shiping Cost: {Shipping_cost} USD")
