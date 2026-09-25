name=("miad")
age=(20)
major=("cs")

if True:
    print(name)
    print(age)
    print(major)
if True:
        print(name)
        print(age)
        print(major)

 #-------------------------------------- comment
        # This is Comment
        print(name) # This is Inline commet

"""
this is
not
multiple
line
comment
"""
#-------------------------------------- types

print(type(10))  #intger
print(type("miad"))  #string
print(type(100.1))  #float
print(type([1,2,3,4,5]))  #list
print(type((1,2,3,4,5)))  #tuple
print(type({"one" : 1, "two" : 2, "three" : 3}))  #dictionary
print(type(2==2))  #boolean

#-------------------------------------- variables

name="miad"  #singl word => normal
myname="miad"  #two word => camelcase
my_name="miad"  #two word => sanke_case

print(name)
print(myname)
print(my_name)

x = 10
x = "hello"
print(x)
                        #print the last one
x = "hello"
x = 10
print(x)

#---------------------------------------------------

#reserved words
help("keywords")

#---------------------------------------------------

a , b , c = 1 , 2 , 3

print(a)
print(b)
print(c)

#---------------------------------------------------

# \b => back space

#bakc space 
print("miad you\bsef") #will remove u because \b removes what comes before it

# \newline => escape new line + \
print("hello \
my name is \
miad")

#escape back slash
print("albaha university \\")

#escape single quote
print('my name is miad \'20\' ')

#escape double quotes
print("my name is miad \"20\" ")

# line feed \n
print("computer sciences \n my major cs") #new line

#carriage return
print("12345\rabcde")
print("123456\rabcde")
print("1234567\rabcde")

#horizontal tap
print("welcome\tback")

#character hex value
print("\x52\x65\x72\x65")
print("\x54\x6F\x74\x69")

#concatenation str+str not str+num
feel = "i really love "
names = "Rere and Toti"

print(feel + names)

a = "one \
two \
three"

b = "first \
second \
third"

print(a + "\n" + b)

#---------------------------------------------------

#strings

mystringone = "this is double quotes"
mystringtwo = 'this is single quote'

mystringthree = "this is double quotes 'my fav' "
mystringfour = 'this is single quote "my fav" '

print(mystringone)
print(mystringtwo)
print(mystringthree)
print(mystringfour)

mystringfive = '''first
second 'my fav num' "my fav num"
third'''

mystringsix = """first
second "my fav num" \\\ 'my fav num' 
third"""

print(mystringfive)
print(mystringsix)

#strings indexing and slicing

# indexing (access single item)

mystring = "miad yousef"

print(mystring[3])
print(mystring[7])
print(mystring[10])

print(mystring[-2])
print(mystring[-6])

# slicing (access multiple sequence items)
#[start:end] #end Not included رقم النهايه مايحسب
#[start:end:steps] => ابد - اوقف وين - اقفز كم

print(mystring[5:8])
print(mystring[7:]) #IF end is not here will go to the end 
print(mystring[:5]) #IF start is not here will  start from 0 
print(mystring[:]) #full data

print(mystring[0::1]) #full data
print(mystring[::1]) #full data
print(mystring[::3])
print(mystring[::2])
print(mystring[2:9:3]) 

#---------------------------------------------------

#strings methods
# len()

a = "computer scinece"
b = "  computer   scinece  "
print(len(a))
print(len(b))

# strip . lstrip . rstrip

a = "   university    "
print(a.strip())
print(a.rstrip())
print(a.lstrip())

a = "&&&&&&university&&&&&"
print(a.strip("&"))
print(a.rstrip("&"))
print(a.lstrip("&"))

a = "&*&*&*university&*&*&*&*&"
print(a.strip("&*"))
print(a.rstrip("&*"))
print(a.lstrip("&*"))

#title() capital even with num
 
a = "i love a4 paper"
print(a.title())

#capitalize() capital without num

a = "i love a4 paper"
print(a.capitalize())

#zfill()

a , b , c , d = "2" , "22" , "222" , "2222"

print(a.zfill(4))
print(b.zfill(4))
print(c.zfill(4))
print(d.zfill(4))

#upper()

a = "momo"
print(a.upper())

#lower()

a = "momo"
print(a.lower())


#split() rsplit()

a = "hello how are you"

print(a.split())

b = "hello-how-are-you"

print(b.split("-"))

c = "hello-how-are-you"

print(c.rsplit("-"))

d = "hello-how-are-you"

print(d.split("-", 2))

d = "hello-how-are-you"

print(d.rsplit("-", 2))

#center()

a = "Nini"
print(a.center(14))
print(a.center(8 , "*"))

#count()

a = "i love my frined remas she is my frined"

print(a.count("frined"))
print(a.count("frined" , 0 , 18 ))


#swapcase()

a = "my age twenty"
b = "MY AGE TWENTY"

print(a.swapcase())
print(b.swapcase())

#startswith()

a = "mom and dad"
print(a.startswith("m"))
print(a.startswith("a",4,))
print(a.startswith("d", 6))
print(a.startswith("o",4))

#endswith()

b = "mom and dad"
print(b.endswith("d"))
print(b.endswith("m",0,3))

#index(substring,star,end)

a = "i am learning python "
print(a.index("e"))
print(a.index("n",12,))
#print(a.index("w")) error

#find(substring,star,end)

b = "i am learning python "
print(b.find("i"))
print(b.find("w")) #-1

#rjust(width,fill charecter)  ljust(width,fill charecter)

a = "Miad"
print(a.rjust(10))
print(a.rjust(10,"~"))

b = "Miad"
print(b.ljust(10))
print(b.ljust(10,"~"))

#splitlines() تجمعه بقوس

a = """frist line
second line
third line"""
print(a.splitlines())

b = "frist line\nsecond line\nthird line"
print(b.splitlines())

#expandtabs() تعطي tap
a = "good\tmorning"
print(a.expandtabs(7))

#istitle() هل كل كلمه تبدا بكبيتل او لا
a = "Meaad Yousef"
print(a.istitle())

b = "meaad yousef"
print(b.istitle())

#isspace()
a = " "
print(a.isspace())

b = ""
print(b.isspace())

#islower()
a = "miad"
print(a.islower())

b = "MIAD"
print(b.islower())

#isidentifier

a = "computer_scinece"
b = "computerscinece200"
c = "computer--scinece"
d = "computer&scinece"

print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())

#isalpha

a = "ddddddlllllll"
print(a.isalpha())

b = "ddddddlllllll0000"
print(b.isalpha())

#isalnum

k = "ddddddgggggg"
print(k.isalnum())

l = "ddddddggggg0000"
print(l.isalnum())

#replace(old value,new value,count)
a = "two two three four two"
print(a.replace("two","2"))
print(a.replace("two","2",2))
print(a.replace("two","2",1))

#joine(iterable)

mylist = ["miad" , "yousf" , "abduallh"]
print("~".join(mylist))
print(" ".join(mylist))
print("-".join(mylist))

#string formatting

name = "miad"
age = 20
rank = 6

print("my name is: " + name)
#print("my name is: " + name + "my age is: " + age) #because str+num false

print("my name is: %s " % "miad")
print("my name is: %s " % name)
print("my name is: %s and  my age is: %d and  my rank is: %d" % (name,age,rank))

# %s => string  %f => float  %d => digit

a = "im student"
b = "university"
c = "computer scincec"
d = 4

print("hello %s in albaha %s my major is %s with %d years" % (a,b,c,d))

#control floting pointn number

mynumber = 2
print("my number is: %.2f" % mynumber)

#truncate string

mylongstring = "hello my name is miad i love you all"
print("message is %s" % mylongstring)
print("message is %.5s" % mylongstring)
print("message is %.13s" % mylongstring)

# الطريقه الحديثه
name = "miad"
age = 20
rank = 6

print("my name is: {} " .format("miad"))
print("my name is: {} " .format(name))
print("my name is: {:s}  and  my age is: {:d}  and  my rank is: {:f}" .format (name,age,rank))

mynumber = 2
print("my number is: {}" .format (mynumber))


mylongstring = "hello my name is miad i love you all"
print("message is {:.3s}" .format (mylongstring))
print("message is {:.9s}" .format (mylongstring))
print("message is {:.1s}" .format (mylongstring))

#rearrange items

a , b , c = "one" , "two" , "three"
print("hello {} {} {}" .format(a,b,c))
print("hello {} {} {}" .format(b,a,c))
print("hello {2} {0} {1}" .format(a,b,c))

# format in version 3.6+
myname = "miad"
myage = 20

print(f"my name is: {myname} and \nmy age is: {myage}")

#numbers

#integer
print(type(10))
print(type(100))
print(type(-10))

#float
print(type(1.0))
print(type(100.8))
print(type(-10.3))

#complex
mycomplexnumber = 2+4j
print(type(mycomplexnumber))
print("real part is: {}" .format(mycomplexnumber.real))
print("imaginary part is: {}" .format(mycomplexnumber.imag))


# 1- you can convert from int to float or complex
# 2- you can convert from float to int or complex
# 3- you cannot convert complex to any type

print(10)
print(float(10))
print(complex(10))

print(10.2)
print(int(10.2))
print(complex(10.2))

print(2+4j)
#print(float(2+4j))
#print(complex(2+4j)) false

#---------------------------------------------------

# arithmetic operators

# + addition
# - subtraction
# * multiplication
# / division قسمه
# % modulus باقي القسمه
# ** exponent الاس
# // floor division القسمه لأقرب عدد صحيح


# Lists 

# list items are enclosed in square brackets العناصر تكون داخل []
# list are ordered , to use index to access item نستخدم الايندكس للوصول لعنصر معين
# list are mutable => add , delete , edit قابله للتعديل
# list items is not unique عادي تتكرر مفس العناصر
# list can have different data types يمدي يكون فيها انواع بيانات مختلفه

mylist = ["one" , "two" , "one" ,3.6 , True ,1]

print(mylist)
print(mylist[1])
print(mylist[-4])

print(mylist[1:4]) # slice
print(mylist[0:4:2])

mylist[2] = 1
mylist[1] = 2
mylist[5] ="one"
mylist[4] ="false"
# mylist[0:2] =["muharam" , "safar"]
print(mylist)

# lists methods
# append()

names =[ "miad" , "taif" , "remas"]
names.append("ghadi")
names.append(15)
names.append(2.9)
names.append(True)

print(names)
print(names[2])
print(names[5])
print(names[4])

#extend()

a = [1,2,3,4]
b = ["a","b","c","d"]
c = ["one" , "two"]

a.extend(b)
a.extend(c)

print(a)

#remove()

a = ["mimi", "roro" , "mimi"]

a.remove("mimi") # just remove one

print(a)

#sort()

a = [3,8,11,-7,199]

a.sort()

print(a)


b = [3,8,11,-7,199]

b.sort(reverse=True) #ترتيب عكس

print(b)

# revers()

v = [3,8,"momo",-7,100]

v.reverse()
print(v)

#clear()

f = [1,2,3,4]

f.clear()

print(f)

#copy

j = [1,2,3,4]
h=j.copy()

print(j) #main list
print(h) #copied list

j.append(5)

print(j) #main list
print(h) #copied list

#count()

b = [4,8,4,6,5,4]

print(b.count(4))

#index()

s = ["mimi", "roro" , "toti"]

print(s.index("roro"))

#insert()

g = [3,8,"momo",9,100]

g.insert(3,"ten") #بتنحط قبل الايندكس الثالث  

print(g)

#pop()

l = [3,8,"momo",9,100]

print(l.pop(3))

#--------------------------------------------------------------------


#conditionals

is_tired = False
need_to_comfort = True

if is_tired and need_to_comfort:
   print("stay at home")
elif is_tired and not need_to_comfort:
   print("go to hospital")
elif not is_tired and need_to_comfort:
   print("stay in your bedroom")
else:
   print("go to work")

#comparisons

def max_num(num1,num2,num3):
 if num1 >= num2 and num1>= num3 : #ماتحقق الشرط
   return num1
 elif num2 >= num1 and num2 >= num3 : # تحقق الشرط الثاني بس فولس و ترو فولس
   return num2
 else :
   return num3 #اذا ماتحقق اي من الشرطين فوق

print(max_num(4,5,7))



def match_string(str1,str2) :
   if str1==str2 :  # هل تساوي
      print("the name is match")
   else:
      print("the name dont match")
    
match_string("miad","miad")



def match_string(str1,str2) :
   if str1!=str2 :  # لا تساوي
      print("the name is dont match")
    
match_string("miad","momo")

#--------------------------------------------------------------------


# while loop

i = 1
while i <= 10 :
   print(i)
   i += 1   # يزود واحد كل مره

print("the loop has ended")


i = 20
while i <= 10 :
   print(i)
   i += 1   
else:
   print("the condition is not true")  # لما الشرط يطلع غلط



# i = 1
# while True :  ارقام لا نهائي
#    print(i)
#    i += 1 

# print("the loop has ended")


i = 1
while i <= 10 :
   i += 1  
   if i == 8:
      continue  # نط من فوق السته
   print(i)

print("the loop has ended")


i = 1
while i <= 10 :
   i += 1  
   if i == 5:
      break  # يوقف عند 5
   print(i)

print("the loop has ended")

#--------------------------------------------------------------------

# for loops

for letter in "miadcs" :  # for معناها لكل 
   print(letter)


myfriends = ["remas" , "taif" , "einas"]

for friends in myfriends :  # friends هنا عادب تكون اي كلمة 
   print(friends)


for x in range(10) : 
   print(x)

for x in range(20,25) : 
   print(x)


myfriends = ["remas" , "taif" , "einas"]
major = "computer scince"

for x in range(len(myfriends)) : 
   print(myfriends[x])



for x in range(20) : 
   if x % 2 == 0 :
     print(x , "is an even number")
   else :
      print(x , "is an odd number")


myfriends = ["remas" , "taif" , "einas"]
for x in range(len(myfriends)) : 
   if myfriends[x] == "einas" :
     print(x , "is einas")
   else :
      print(x , "is not einas")



myfriends = ["remas" , "taif" , "einas"]
for x in myfriends : 
   if x == "ghadi" :
     print(x , "is your friend")
     break
else :
      print("not found")



for x in range(1,5) : 
   if x == 3 :
     continue
   print(x , "is this true number")

   #------------------------------------------------------------

   # functions

def say_hi():
   print("hello user")

print("oh")
say_hi()
print("how are you?")


def say_hi(name , age):
   print("hello " + name + " your age is " + age)

say_hi("remas" , "20")


def digit (number):
   return number*number*number

print(digit(2))


def sum (num1,num2):
   return num1+num2  # مارح يتحقق اي امر بعد الريترن

print(sum(2,2))

name = "miad"
print(name)

print("github")





