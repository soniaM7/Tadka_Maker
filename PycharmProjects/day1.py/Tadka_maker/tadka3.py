# This the final tadka maker

import logging

from Spieces import Spieces
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

logging.info('Customer logged in')

print "\n" + "Welcome to Tadka Maker"

def choose():

    print "\nChoose: "
    choose = ["0. Invalid","1. North Indian", " 2. South Indian"," 3. chinese", " 4. Italian"]
    print choose[1:4]
    option = int(raw_input())
    print "Your selected Menu is: "
    print choose[option]
    if option == 1:
        logging.info('Dish is selected')
        def dish():
            print "\nChoose Dishes: " \
                  "\n 1. Allu Gobhi" \
                  "\n 2. Allu Matar" \
                  "\n 3. Allu ShimlaMirch" \
                  "\n 4. Halwa"
        dish()

choose()

choose_dishes = ["Select in between 1 to 4","Allu Gobhi", "Allu Matar", "Allu ShimlaMirch", "Halwa"]

dish = int(raw_input())

print "Your selected Dish is: "
#print choose_dishes[i]

Spieces = Spieces(choose_dishes[dish])

print Spieces.Vegi_name




print "\n Required ingredients for the dish are :  1.Onion, 2.Tomatto, 3.Potato, 4.Ginger, 5.Garlic, 6.Green chilly, 7.Haldi, 8.Jeera,9.Oil"

def spieces_masala():
    ingeredent_number = int (raw_input("Please enter ingredients by their number: "))
    masala = ["Select in between 1 to 9", "1.Onion", "2.Tomatto", "3.Potato", "4.Ginger", "5.Garlic", "6.Green chilly",
              "7.Haldi", "8.Jeera,9.Oil"]

    Spieces.spieces_masala.append(masala[ingeredent_number])
    option_new = raw_input("Do you want to add more: press y or n")
    if option_new == "y":

        spieces_masala()
    else:
        print "\n Here is your selected ingredients"
        logging.warning('Order finished')

        print "\n Your dish will be deliver to your address with selected ingredients"

option = raw_input("Do you want to customise Dish: press y or n ")

if option == "y":
    spieces_masala()
    print Spieces.spieces_masala



































'''
   
    
    bucket = AlluGobhi("1.Onion", "2.Tomatto", "3.Potato", "4.Ginger", "5.Garlic", "6.Green chilly", "7.Haldi",
                       "8.Jeera",
                       "9.Oil")
    my_bucket=[]

    if choose_dishes[0]:
        option=raw_input("If you want to customise press yes else No")
        if option=="yes":

            my_bucket=[]
            a = int(raw_input("How many ingredients do you want to skip"))

            if a >= 0:
                if a==1:
                    my_bucket = bucket.one
                    my_bucket
                    print my_bucket
                    a=a-1


'''