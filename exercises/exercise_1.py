# Exercise 1
# Your solution comes here

num = int(input('Please enter a five digit number'))
first = (num // 10000) % 10
second = (num // 1000) % 10
third =  (num // 100) % 10
fourth = (num // 10) % 10
fifth =  (num) % 10
print(first , second, third, fourth, fifth)

new_num = str(first + third + fifth) + str(second + fourth) 

print(new_num)

