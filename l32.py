import math
for x in range(10, 90, 5):
    a = math.sin(4**(x/100) - math.log(3*(x/100)))
    b = math.log(4, 3*(x/100))
    y = a+b
    print(y)