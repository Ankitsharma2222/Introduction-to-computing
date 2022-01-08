#Assignment 1
#Name=Ankit sharma(21103021)
#question 1

first_number=float(input("enter first number: "))
second_number=float(input("enter second number: "))
third_number=float(input("enter third number: "))
average=(first_number+second_number+third_number)/3
print("average is: ", average)




#question 2

gross_income=float(input("Gross income: "))
tax_rate=20/100
standard_deduction=10000
deduction_per_dependent=3000
number_of_dependent=int(input("Number of dependents: "))
taxable_income=gross_income - standard_deduction - (deduction_per_dependent*number_of_dependent)
#calculating tax

tax=taxable_income*tax_rate
print("your income tax: " ,tax)


#question 3


sid=input("Enter your SID: ")
name=input("Enter your name: ")
#in gender M implies male and F implies female

gender=input("Enter your gender: ")
cgpa=input("Enter your cgpa: ")
print([sid,name,gender,cgpa])



#question 4


student1_marks=int(input("Student 1 marks: " ))
student2_marks=int(input("Student 2 marks: " ))
student3_marks=int(input("Student 3 marks: " ))
student4_marks=int(input("Student 4 marks: " ))
student5_marks=int(input("Student 5 marks: " ))

list=[student1_marks, student2_marks, student3_marks, student4_marks, student5_marks]

#to sort list we use a inbuilt function sort

list.sort()
print("List is: ",list)



#question 5(a)

color=['Red','Green','White','Black','Pink','Yellow']

#to remove for 4th element we use pop(index of element which we want to remove) function
#index of 4th element is 3

color.pop(3)
print(color)


#question 5(b)

color=['Red','Green','White','Black','Pink','Yellow']
#replacing Black and Pink with Purple
color[3:5]=['Purple']
print(color)

