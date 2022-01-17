a = int(input('Input side a of a triangle '))
b = int(input('Input side b of a triangle '))
c = int(input('Input side c of a triangle '))
p = (a+b+c)/2
s = (p*(p-a)*(p-b)*(p-c))**0.5
print('Area of triangle is ', s)