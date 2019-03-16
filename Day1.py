##math
# #minute to seconds converter
# print("Enter time in minutes")
# minutes = input()
# seconds = float(minutes)* 60
# print("There are {} seconds in a minute".format(seconds))

# # date/time
# import datetime
# now = datetime.datetime.now()
# print(now.hour,"hours", now.minute,"minutes", now.second, "seconds")
# print(now.year)
#
# # volume calculator
# import math
# print("Enter the desired radius")
# radius = int(input())
# volume = (4/3)*math.pi*math.pow((radius),3)
# print("The volume of your sphere is {:.2f}".format(volume))

# print("Input a base and a power")
# base = int(input())
# power = int(input())
# length_of_number = len(str(base**power))
# print(base**power)
# print(length_of_number)

# import random
# print("input the lower and upper bound")
# lb = int(input())
# ub = int(input())
# # print(random.random()*(ub-lb)+lb)
# print(random.randint(lb, ub))
# print(random.choice([1,2,3,4,5,6]))

## Strings
# \n - new line
# \ - keep apostrophe
# print('I am saying I am \'OK\'')
# print("Hi!\nMy name is Shashwat")

## Boolean - important for conditional statements
# print(3>2)
# print(3>5)
# print(3 > 2 and 3 > 5)
# print(3 > 2 or 3 > 5)

# Virtual Bouncer
age = int(input("How old are you?"))
location = input("Are you located in the greater boston area? ")
timeleft = (21 - age)
if age >= 21 and location == 'yes':
    print('Your all set! Time to party!')
elif age < 21 and location == 'yes':
    print("Sorry, you have to wait for {} year!".format(timeleft))
    if timeleft == 1:
        print("Sorry, you have to wait for {} more year!".format(timeleft))
    else:
        print("Sorry, you have to wait for {} more years!".format(timeleft))
elif age < 21 and location == 'no':
    if timeleft == 1:
        print("Sorry, you have to wait for {} more year and move to boston!".format(timeleft))
    else:
        print("Sorry, you have to wait for {} more years and move to boston!".format(timeleft))
elif age >= 21 and location == 'no':
    print("Sorry, you are too far away from us!")

# == is literally equal to
# != is not equal to



