#Author: Jacob Peel
#Program Description: Material purchase recommendations for greatest revenue.

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

        company_dict[id] = name
        quantity_dict[id] = quantity
        price_dict[id] = price

    materials_file.close()

    print(company_dict)
    print(quantity_dict)
    print(price_dict)

#Call main
main()
        
