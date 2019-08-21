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

north_indian_dishes = ["1. Allu Gobhi", "2. Allu Matar", " 3. Allu ShimlaMirch", " 4. Halwa"]
south_indian_dishes = ["1. Masala Dosa", "2. Bisibili Bhat", " 3. Idali Sambhar", " 4. Rasam"]
chinese_dishes = ["1. Nodules", "2. Spring Rolls", " 3. Dumplings", " 4. Fried Mashi"]

food_option = [vegitable(menu[1], north_indian_dishes),
               vegitable(menu[2], south_indian_dishes),
               vegitable(menu[3], chinese_dishes)
               ]
def call_manu(menu):

    for menu in food_option:
        print menu.food_option
        print menu.dishes
        print "\n"

call_manu(menu)


menu_option = int(raw_input())

print "your selected food is \n" + menu[menu_option]











'''

for show_menu in food_option:
    count =0
    print menu[count]
    print "\n"
    print food_option[count].dishes
    print "\n"
    count = +1
'''

'''

print food_option.food_option


menu1="\n 1. Allu Gobhi" \
                   "\n 2. Allu Matar" \
                   "\n 3. Allu ShimlaMirch" \
                   "\n 4. Halwa"

north_indian_menu = north_indian_food(menu1)
print north_indian_menu.dish_name

'''

'''

from Question_Round2 import Question_Round2

question_prod = [ "What is the capital of Italay?  \n a). Tokyo  \n b), Moscow  \n c). Rome  \n d). canberra ",
                  "\n What is the capital of Argentina ? \n a). Buenos Aires  \n b), Seoul \n c). Rabat \n d). canberra ",
                    "\n What is the capital of Wales ? \n a). Cardiff \n b), Seoul  \n c). Nairobi  \nd). Suva "
]


questions = [
              Question_Round2(question_prod[0] , "c"),
              Question_Round2(question_prod[1] , "a"),
              Question_Round2(question_prod[2] , "a")
]

def test_run(questions):
    score = 0
    for question in questions:

        answer = raw_input(question.prod)
        if answer == question.answers:

            score = score + 1

    print ("you got " + str(score) + "/" + str(len(questions)) + "correct")
    #print "you have" + str(round) + "correct answer"


test_run(questions)



'''
