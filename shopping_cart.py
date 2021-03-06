# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Setup project repository
#test2

import datetime

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017
# TODO: write some Python code here to produce the desired functionality...

#code to make sure individual products are printing correctly

pre_tax = 0
pre_tax_dollar=0


#creating place to store all products purchased

total_products = []

#User Product Inputs

user_product = []

now = datetime.datetime.now()

while user_product != "DONE":
    user_product = (input("Please input your product's number: "))
    if user_product != "DONE":
        if int(user_product) <=21:
            total_products.append(user_product)
        else:
            print("Sorry! That is not a real product number. Please input a new number!")


#Grocery Store Header and Time
print("\n")
print("******************")
print("Gleason's Grocery")
print("3700 O Street NW")
print("Call us at (610)867-5309")
print("Time of Checkout Start: " + str(now.strftime("%m/%d/%Y %I:%M %p")))
print("******************")


#Printing Product List


def dollar_format(prices):
    return "${0:,.2f}".format(prices)

print("Your purchases: ")

for user_product in total_products:
    product_lookups = [p for p in products if str(p["id"]) == str(user_product)]
    product_lookup = product_lookups[0]
    print(str(product_lookup["name"]) + ":  " + str(dollar_format(product_lookup["price"])))
   
    pre_tax = pre_tax + product_lookup["price"]
    pre_tax_dollar = dollar_format(pre_tax)

print("******************")
print("PRE-TAX PRICE: " + str(pre_tax_dollar))


#Tax Calculation
tax_rate = 0.06
tax_amount = pre_tax * tax_rate
tax_amount_formatted = dollar_format(tax_amount)

print("TAX: " + str(tax_amount_formatted))
print("******************")

#Total Cost Calculation
total_cost = pre_tax + tax_amount
total_cost_formatted = dollar_format(total_cost)
print("TOTAL PRICE: " + str(total_cost_formatted))
print("******************")

print("THANK YOU FOR SHOPPING WITH US. WE'LL SEE YOU NEXT TIME!")

product_lookup[0] = 0