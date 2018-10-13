from math import sqrt

def isPalindrome(number):
    number = str(number)
    if number == number[::-1]:
        return True
    return False

def isSquare(number):
    number = int(number)
    rt = sqrt(number)
    if int(rt) == rt:
        return True
    return False

def pal_from(start, end):
    pals = 0
    for i in range(start, end+1):
        if isPalindrome(i) and isSquare(i) and isPalindrome(int(sqrt(i))):
            pals+=1
    return pals

with open('C-small-attempt0.in') as f:
    number = int(f.readline())
    for case in range(number):
        data = f.readline()
        start, end = data.split()
        print("Case #{}: {}".format(case+1, pal_from(int(start), int(end))))

