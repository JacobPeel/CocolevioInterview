#Author: Jacob Peel
#Program Description: Material purchase recommendations for greatest revenue.

#Import company class
import company

#Declare constants
MATERIALS_REQUESTS_DATA = "MaterialRequests.txt"

#Define main function
def main():

    #Open input file
    materials_file = open(MATERIALS_REQUESTS_DATA, 'r')

    #Create company dictionary
    company_dict = {}

    #Create quantity dictionary
    quantity_dict = {}

    #Create price dictionary
    price_dict = {}

    #Create unit price dictionary
    unit_price_dict = {}

    #Create purchasers list
    purchasers_list = []

    #Add elements to purchasers list
    for x in materials_file:
        purchasers_list.append(x.strip().split(','))

    #Assign elements to variables
    for element in purchasers_list:
        id = element[0]
        name = element[1]
        quantity = element[2]
        price = element[3]

        unit_price = str((float(price))/(int(quantity)))

        my_company = company.Company(id, name, quantity, price, unit_price)
        company_dict[id] = my_company
        quantity_dict[id] = quantity
        price_dict[id] = price
        unit_price_dict[id] = unit_price

    materials_file.close()

    print_menu(company_dict)

def print_menu(company_dict):

    print(" This program calculates the per unit price that each \n company is willing to purchase one unit of material \n from the data given in the MaterialsRequest.txt file. \n In order to maximize profits it is suggested that you \n sell to the companies with the greatest unit price offer.")
    print()
    #Print menu
    menu_heading = "{:<18}{:<8}{:<10}{:<10}".format("Name", "Qty", "Price", "Unit Price")
    print(menu_heading)
    for x in company_dict:
        print(company_dict[x])

#Call main
main()
        
