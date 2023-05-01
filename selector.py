import random

num = int(input("count plz:"))

for i in range(num):
    print(i, random.sample(range(1,45),6))
