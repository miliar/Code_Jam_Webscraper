def checker(n):
    a = []
    for i in range(0,len(str(n))):
        a.append(int(str(n)[i]))
    if sorted(a) == a:
        return True
    return False

def zero(n):
    a = []
    for i in range(0,len(str(n))):
        a.append(int(str(n)[i]))
    for i in a:
        if i > 1:
            return False
    if len(a) == 1 and a[0] == 1:
        return False
    return True

def convert(n):
    l = len(str(n))-1
    s = ""
    for i in range(0,l):
        s += "9"
    return int(s)

def last(num):
    for i in range(num,0,-1):
        if zero(i):
            return convert(i)
        if checker(i):
            return i
    return 0

l = int(input())

for i in range(0,l):
    num = int(input())
    print("Case #{}: {}".format(i+1,last(num)))
