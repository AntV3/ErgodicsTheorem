import random
##  example of ergodics  theorem
total = 0
num_iterations = 10000

for i in range(num_iterations):
    random_num = random.random()
    total += random_num

average = total / num_iterations
print("The average value of the random numbers is:", average)