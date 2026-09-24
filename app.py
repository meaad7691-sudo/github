print("*" * 10)

name = "john smith"
age = 20
is_new = True

print(name)
print(age)
print(is_new)

# name = input('whats your name? ')
# print('hello ' + name)


# name = input('whats your name? ')
# color = input('whats your fav color? ')

# print(name + " likes " + color)


# weight_lbs = input('weight(lbs): ')
# weight_kg =int(weight_lbs) * 0.45
# print(weight_kg)

name = "jennifer"
print(name[1:-1])

first = 'MIAD'
last = 'ALZHRANI'
message = last + ' [' + first + '] is a Cs ' 
messagetwo = f'{last} [{first}] is a Cs '
print(message)
print(messagetwo)

# string methods
name = "miad yousef alzhrani"
# len()
print(name.upper())
print(name.lower())
print(name.title())
print(name.find('m')) # يعثر على
print(name.replace('alzhrani', 'alghbishi')) #يحل محل 
print('yousef' in name)
print('remas' in name)



x = 2.9
print(round(x)) #  تقريب لعدد صحيح
print(abs(-2.9)) # القيمه المطلقه

import math
print(math.ceil(2.5)) # تقريب للاعلى 
print(math.floor(2.5)) # تقريب للاسفل


# grade = int(input("Enter your grade: "))
# if grade >= 90:
#  print("A")
# elif grade >= 80:
#  print("B")
# elif grade >= 70:
#  print("C")
# elif grade >= 60:
#  print("D")
# else :
#  print("F")


house_price = 1000000
has_good_credit = True
if has_good_credit :
  down_payment = house_price*10/100
else:
  down_payment = house_price*20/100
print(down_payment)
 









