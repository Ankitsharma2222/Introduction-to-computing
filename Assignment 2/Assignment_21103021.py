# NAME=>ANKIT SHARMA,
# SID=>21103021,
# DEPT.=> CSE
#assignment>>2



#Question.1

input_string="Python is a case sensitive language"

# (a) part
#to find the length of string we use a inbuilt funtion len()

print(len(input_string))

#(b) part

# to reverse the string we use slicing method

print(input_string[::-1])

#(c) part
# to make a new string of " a case sensitive " we use slice method
# index of 'a' is 10 and index of 'e' in sensitive is 25

new_string=input_string[10:26]   # word at index 26 is excluded

#to prove our code we print new_string

print(new_string)

#(d) part
# to replace "a case sensitive" by "a object oriented" we use a inbuit funtion named as replace()

print(input_string.replace('a case sensitive', 'a object oriented'))

#(e) part
#to find index of "a" in input_string we use find() function

print(input_string.find('a'))

#(f) part
# to remove whitespaces we again use replace() function

print(input_string.replace(" ",""))






#Question.2

name="Ankit sharma"
sid=21103021
cgpa=9.9
 #using formatted strings

print(f'''Hey,{name} is Here!
My SID is {sid}
I am from CSE department and my CGPA is {cgpa}''') 




#Question.3
a=56
b=10
#(a)
print(a&b)

#(b)
print(a|b)

#(c)
print(a^b)

#(d)
a = a << 2
b = b << 2

#(e)

a = a >> 2
b = b >> 4


      


#Question.4

#firtly we take input and make a list of nubers given by user

numbers=[]
for count in range(3):
    a=float(input("Please enter your number: "))
    numbers.append(a)
max=numbers[0]            #here we assume that number at index 0 is greatest    
for number in numbers:
    if number > max:
        max=number
print("Greatest number is : ", max)    





 #Question.5

entry=input("enter someting : " )

#now we make a list named as lis of seperate words present in entry using inbuilt funtion split()

lis=entry.split()

#now we use for loop to check "name" is present in user entry

for word in lis:
    if word == "name":
        print(" yes")
        break  #if name is present then we break next iterations

else:
     print("No")



#Question.6

# len_1 means length of first side

len_1=int(input("Enter side length: "))
len_2=int(input("Enter side length: "))
len_3=int(input("Enter side length: "))

if len_1 + len_2 > len_3 and len_1 + len_3 > len_2 and len_3 + len_2 > len_1 :
    print("YES,triangle can be formed")
else:
    print("NO,triangle can not be formed")
  
    
