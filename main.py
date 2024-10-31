# TASK-1: Fibonacci Sequence Generator

total_terms = int(input("Enter number of terms: "))

first_term = 0
second_term = 1
count = 0

if total_terms <= 0:
   print("Wrong input! Please enter a positive integer")

elif total_terms == 1:
   print("Fibonacci sequence upto",total_terms,":")
   print(first_term)

else:
   print("Fibonacci sequence:")
   while count < total_terms:
       print(first_term)
       nth_term = first_term + second_term
       
       first_term = second_term
       second_term = nth_term
       count += 1
