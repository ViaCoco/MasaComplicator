def age_score(years):
	if years < 20:
		return 3
	elif years < 50:
		return 1
	else:
		return 2

def fb_score(friends):
	if friends < 200:
		return 1
	elif friends < 600:
		return 2
	else:
		return 3

def family_score(members):
	if members < 3:
		return 1
	elif members < 6:
		return 2
	else:
		return 3

def deadlines_score(aproaching):
	if aproaching == "Yes":
		return 3
	else:
		return 0

def money_score(balance):
	if balance < 0:
		return 3
	elif balance < 300:
		return 1
	else:
		return 0

def bus_score(busses_missed):
	if busses_missed == "Yes":
		return 3
	else:
		return 0

def internet_score(happy_with_speed):
	if happy_with_speed == "Yes":
		return 0
	elif happy_with_speed == "Somewhat":
		return 1
	else:
		return 3


def calculate_complexity(score_sum):
	if score_sum < 10:
		return "You have it easy!"
	elif score_sum < 16:
		return "Your life is complicated!"
	else: 
		return "It's hard to be you!"


cur_age = raw_input("How old are you?")
#print age_score(cur_age)

score_age = age_score(int(cur_age))
print score_age

FB_friends = raw_input("How many FB friends do you have?")
#print fb_score(FB_friends)

score_fb = fb_score(int(FB_friends))
print score_fb

family_members = raw_input("How many family members do you have?")
#print family_score(family_members)

score_family = family_score(int(family_members))
print score_family

deadlines_aproaching = raw_input("Do you have any deadlines aproaching? Yes/No")
#print deadlines_score(deadlines_aproaching)

score_deadlines = deadlines_score(deadlines_aproaching)
print score_deadlines

money_balance = raw_input("How much euros do you have in your bank account?")
#print money_score(money_balance)

score_money = money_score(int(money_balance))
print score_money

missed_busses = raw_input("Do you often run after the bus and miss it anyway? Yes/No")
#print bus_score(missed_busses)

score_bus = bus_score(missed_busses)
print score_bus

internet_speed = raw_input("Are you happy with your internet speed? Yes/No/Somewhat")
#print internet_score(speed)

score_internet = internet_score(internet_speed)
print score_internet

score = score_age + score_fb + score_family + score_deadlines + score_money + score_bus + score_internet
result = calculate_complexity(score)
print score
print result







import datetime

datetime = datetime.datetime.now
#deadlines = raw_input("Do you have a deadline aproaching? Yes/No")-------------
#missed_busses = raw_input("Do you often run after the bus and miss it anyway? Yes/No")------------
#money = raw_input("How much money do you have in your bank account?")-----------
#job = ["loving it", "hating it", "don't know"]
#family_members = raw_input("How many family members do you have?")-------------
#temperature = raw_input("How many degrees Celius is outside?")
#internet_speed = raw_input("Are you happy with your internet speed?")------------
#FB_friends = raw_input("How many FB friends do you have?")----------------
#cur_age = raw_input("How old are you?")--------------------


#if deadlines == "No":
#    deadlines = False
