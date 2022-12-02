
#exercise 1
""" 
def bigger(a, b, c):
    if a > b and a > c:
        return (a)
    elif b > a and b > c:
        return (b)
    else:
        return (c)

a = int(input("type first number...  "))
b = int(input("type second number... "))
c = int(input("type third number...  "))
print (bigger (a, b, c))
"""

#exercise 2
""" 
def listChecker(list):
    i = 0
    j = 0
    x = 0 
    while i < len(list):
        if list[i] == 19:
            j += 1
        if list[i] == 5:
            x += 1
        i += 1
    if j == 2 and x >= 3:
        return True
    else:
        return False

list = [19, 19, 3, 5, 5, 5, 7, 8]
print (listChecker(list))
"""

#exercise 3
""" 
def powerModule(integer):
    if integer > 16 and integer % 34 == 4:
        return True
    else:
        return False

a = int(input("N: "))
print(powerModule(a))
"""
#exercise 4
""" 
def maxLength(list):
    i = max (list, key = len)
    return i

list = ["ola", "adeus", "maior"]
print(maxLength(list))        
"""

#exercise 5