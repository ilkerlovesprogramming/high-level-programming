# 1. Create variable named x and assign value = 4
x = 4
#2. Create variable named y and assign value = 2
y = 2
#3. Print x + y
print(x+y)
#4. Create a variable named car_name and assign value “Mercedes”
carname = "Mercedes"
#5. Create a variable named num_wheels and assign value of 4
num_wheels = 4
#6. Print f-string with car_name and num_wheels
print(f"{carname} has {num_wheels} wheels")
#7. Create variable named name and assign value of your name
name = 'Ilker'
#8. Create variable named num_apples and assign value of 24
num_apples = 24
#9. Create variable named num_friends and assign value of 7
num_friends = 7
#10. Print f-string with name, num_apples, num_friends, and apples_per_friend
apples_per_friend= num_apples/num_friends
print(f'{name} has {num_apples} apples and {num_friends} friends and each friend can get {apples_per_friend}')
#11. Create variable named bill total and assign value of 120
bill_total = 120
#12. Print f-string with num_people, bill_total, and cost_per_person formatted to 2 decimal places
num_people = num_friends
cost_per_person = bill_total/num_people
#13. Print f-string with num_people, bill_total, and cost_per_person formatted to an int
print("{} people will share {} bill with {} for each person.".format(num_people, bill_total, round(cost_per_person)))
"""

Actually I would try int(cost_per_person) but it is not efficient. 
Problem: When you go over 17.5 it will be 17 but its need to be 18
That is why I used built-in function which is round()
:)
"""
#14. Create variable named dessert_cost and assign value = 6.55
dessert_cost = 6.55
#15. Print f-string with num_people, dessert_cost, and total_cost_of_desserts formatted to 2 decimal places
total_cost_of_desserts = (num_people*dessert_cost)
print(f"{num_people} ate a desert with {dessert_cost} for each and total bill was {total_cost_of_desserts: .2f}")
