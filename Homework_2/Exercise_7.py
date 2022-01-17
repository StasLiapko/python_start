x = int(input("Input number: "))
s = 0
while (x != 0):
    s = s + x % 10
    x = x // 10
print("Sum of digits in a number is: ", s)