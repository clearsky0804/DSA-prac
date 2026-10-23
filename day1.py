# print("hello World")

# nums = [4 , 7, 1]

# for i in enumerate(nums): # (prints both position and value, pos first) -- if only one variable, it produces a tuple(pos, value)
#     print(i)
#     print(type(i))

# if not nums:
#     print("empty_list")



# Fizz Buzz

# i = 1
# while i < 20:
#     if i % 15 == 0:
#         print(f"{i} FizzBuzz")
#     elif i % 3 == 0:
#         print(f"{i} Fizz")
#     elif i % 5 == 0:
#         print(f"{i} Buzz")
#     i = i + 1
    
# i = 1
# sum = 0
# while i <= 100:
#     if i % 2 == 0:
#         sum = sum + i
#     i = i + 1
# print(sum)


# a = [ 57 , 99 , 78 , 54 , 102]

# asm = a[0]

# for every_num in a:
#     if asm < every_num:
#         asm = every_num
# print(asm)

# Practice On Loops

# 1) Countdown. Print 10 down to 1, then Liftoff!, using range with a step of -1. 

# for i in range(10 ,0, -1):
#     print(i)
# print("liftoff!")

# 2. Ticket price. Set an age variable 
# and print the ticket price: under 5 is free, 
# 5 to 17 pays 100, 
# 60 and over pays 150, 
# and everyone else pays 250. 
# Test with ages 3, 12, 30 and 65. You should get 0, 100, 250, 150

# age = 65

# if age < 5:
#     print(age)
# elif age >= 5 and age <= 17:
#     print("Ticket is 100")
# elif age > 60:
#     print("Ticket is 150")
# else: 
#     print("Ticket is 250")


# 3. Sum and average. For n = 10, 
# use a loop (not sum()) to add up the numbers 1 to n, then print the total and the average. Expected: 55 and 5.5.

# n = 10
# i = 1
# sum = 0 
# while i <= n:
#     sum = sum + i
#     i = i+1

# print(f"{sum} is sum")
# print(f"{sum/n} as average")

# 4. Times table. Print the 7 times table in this format:
# 7 x 1 = 7
# 7 x 2 = 14
# ...
# 7 x 10 = 70

# i = 1
# n = 10 

# while i <= n:
#     print(f"7 * {i} = {7 * i}")
#     i = i + 1

# 5. Vowel counter. 
# Count the vowels in "databricks is fun" by looping over the string. Expected: 5. Hint: if ch in "aeiou":.

# stmn = 'databricks is fun'
# # vowels = ['a' , 'e' , 'i', 'o', 'u']
# vowels = 'aeiou' # also works (it will take it as alist)
# counter = 0

# # this does not consider lower case, so instead go with stmn.lower()
# for every_char in stmn:
#     if every_char in vowels:
#         counter = counter + 1
# print(counter)

# 7. First match.
# Use a while loop and break to find the first number above 100 that’s divisible by both 7 and 9. Expected: 126.

# i = 100

# while True:
#     if i % 63 == 0:
#         break
#     i += 1
# print(i)
    
# 8.print the below pattern
# *
# **
# ***
# ****

# n = 4
# i = 1

# while i <=n :
#     print('*'*i)
#     i += 1

# # reverse

# n = 4
# i = 1

# while n>=i:
#     print('*'*n)
#     n -= 1

# 9. Primes. 
# Write a loop that checks whether a number is prime, 
# then use it to print every prime from 1 to 30. Expected: 2 3 5 7 11 13 17 19 23 29. Watch out: 1 is not prime.



n = 30 
i = 3
counter = 0
prime = [2]

while i <= n:
    counter = 0
    for every_num in range(2,i):
        if i % every_num == 0:
            counter = 1
            continue
    if counter == 0:
        prime.append(i)
    i+= 1


print(prime)








