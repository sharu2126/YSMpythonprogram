 #Write a function greet(name) that takes a name ehich is store in variable as input and prints "Hello, [name]!".

##def greet(name):
##    print("Hello",name)
##greet("Siddhi")

#2. Create a function square(num) that returns the square of a given number.

##def square(num):
##    return num*num
##print("Square of a num:",square(5))


#3. Write a function is_even(n) that returns True if a number is even, otherwise False.

##def is_even(n):
##    if n%2==0:
##        return True
##    
##    else:
##        return False
##print("Given no is Even",is_even(5))

#4. Define a function sum_numbers(a, b=10) that takes two numbers and returns their sum. If the second number is not provided, it should default to 10.


##def sum_numbers(a,b=10):
##    return a+b
##print("sum of two numbers is",sum_numbers(5,5))


#5. Write a recursive function factorial(n) to calculate the factorial of a number.

##def fact(n):
##    if n==0 or n==1:
##        return 1
##    return n*fact(n-1)
##print("factorial is :",fact(5))


#6. Use a lambda function with filter( ) to get all even numbers from a list: [1, 2, 3, 4, 5, 6, 7, 8].

##def even_odd(i):
##    if i % 2 == 0:
##        print(i,"no is even")
##    else:
##        print(i,"no is odd")
##
##n = [1, 2, 3, 4, 5, 6, 7, 8]
##
##for num in n:
##    even_odd(num)

#7. Write a while loop to print the first 5 multiples of 3.

##n=1
##while n<=5:
##    print(n*3)
##    n+=1


#8. Create a loop that prints all numbers from 1 to 20 but skips multiples of 5

##n=1
##while n<=20:
##    if n%5==0:
##        n+=1
##        continue
##    print(n)
##    n+=1


#9. Write a loop that stops when it encounters the number 7 in this list: [1, 2, 3, 4, 5, 6, 7, 8, 9].

##n=[1,2,3,4,5,6,7,8,9]
##for num in n:
##    if num==7:
##        break
##    print(num)

#10. Write a program that checks if a year is a leap year. (Hint: A year is a leap year if it is divisible by 4 but not by 100, except when it is also divisible by 400.)

##def is_leap_year(year):
##    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
##        print(year, "is a leap year")
##    else:
##        print(year, "is not a leap year")
##
##
##year = int(input("Enter a year: "))
##is_leap_year(year)



    



