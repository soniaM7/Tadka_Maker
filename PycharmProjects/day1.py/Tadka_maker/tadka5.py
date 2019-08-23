# This the  tadka maker v2

from vegitable import vegitable
from spieces4 import Spieces4
from north_indian_food import north_indian_food
import logging

logging.basicConfig(format='%(asctime)s  %(message)s', level=logging.INFO)

logging.info("customer is logged in")

print "\nWelcome to Tadka Maker version:2\n"
print "Choose your food: \n"
menu = ["Choose your Food","1: North Indian", "2: South Indian", "3: Chinese"]

north_indian_dishes = ["1. Allu Gobhi", "2. Allu Matar"]
south_indian_dishes = ["1. Masala Dosa", "2. Bisibili Bhat"]

north_Allu_gobhi_ingredients = ["1.Onion", "2.Tomatto", "3.Potato", "4.Ginger", "5.Garlic", "6.Green chilly","7.Haldi", "8.Jeera,9.Oil"]
north_Allu_matar_ingredients = ["1.Matar", "2.Potato", "3.Ginger", "4.Ginger", "5.Garlic", "6.Green chilly","7.Haldi", "8.Jeera,9.Oil"]

south_dosa_ingredients = ["1.Onion", "2.Tomatto", "3.Potato", "4.Ginger", "5.Garlic", "6.Green chilly","7.Haldi", "8.Jeera,9.Oil"]
south_bhat_ingredients = ["1.Matar", "2.Potato", "3.Ginger", "4.Ginger", "5.Garlic", "6.Green chilly","7.Haldi", "8.Jeera,9.Oil"]

food_option = [
    vegitable(menu[1],north_indian_dishes,north_Allu_gobhi_ingredients),
    #vegitable(menu[1],north_indian_dishes[1:2],north_Allu_matar_ingredients),
    vegitable(menu[2],south_indian_dishes,south_dosa_ingredients) #,
    #vegitable(menu[2],south_indian_dishes[1:2],south_bhat_ingredients)
              ]

full_menue = [
    vegitable(menu[1],north_indian_dishes[1:2],north_Allu_gobhi_ingredients),
    vegitable(menu[1],north_indian_dishes[1:2],north_Allu_matar_ingredients),
    vegitable(menu[2],south_indian_dishes[1:2],south_dosa_ingredients),
    vegitable(menu[2],south_indian_dishes[1:2],south_bhat_ingredients)
              ]

def show_food(food_option):

    for order in food_option:
        print order.food_option
        print order.dishes
        print "\n"

show_food(food_option)

def order_place(food_option):
    for order in food_option:

        number = int (raw_input())
        print "Selected Food is: \n" + menu[number]
        print "\nSelect your dish:"
        print order.dishes[0]
        print order.dishes[1]
        dish_number = int(raw_input())
        return dish_number

dish_number = order_place(food_option)



def select_dish():


    if dish_number ==1:
        print "Selected dish is" + north_indian_dishes[0]
    elif dish_number == 2:
        print "selected dish is" + north_indian_dishes[1]
    elif dish_number ==0 or dish_number != 1 and 2:
        print "wrong option!! Try again.."


select_dish()


'''


is_male= False
is_tall= True


if is_male and is_tall:
    print "you are a male and tall too"
elif is_male and not(is_tall):
    print "you are male but not tall"
elif not(is_male) and is_tall:
    print "you are not male but talll"

else:
    print "you are neither male nor tall"

'''




'''

def select_dish(full_menu):
    
    for order in full_menue:
        if select ==menu[1]:
            vegitable(north_indian_dishes[0],north_Allu_gobhi_ingredients)
            print order.req_ingredients



select_dish(full_menue)

'''