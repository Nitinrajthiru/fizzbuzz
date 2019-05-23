nums = [3, 5]
max = 100
result = 0
for num in nums:
    for i in range(1,max):
        if num*i < max:
print("fizz")


result = 0
for i in range(0,max):
    if i%3 == 0 or i%5 == 0:
print("buzz")
