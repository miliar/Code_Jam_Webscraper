from sys import stdin

cases = int(stdin.readline())
case = 1

def converter(n):
    s = str(n)
    s = list(s)
    for i in range(1,len(s)):
        if s[i] < s[i-1]:
            index = i
            break
    for i in range(index,len(s)):
        s[i] = "0"
    newn = ""
    for i in s:
        newn += i
    newn = int(newn) 
    return newn

def isTidy(n):
    s = str(n)
    s = list(s)
    if s == sorted(s):
        return True
    else:
        return False

for c in range(cases):
    n = int(stdin.readline())
    a = False
    while not a:
        if isTidy(n):
            a = True
        elif isTidy(n-1):
            n -= 1
        else:
            n -= 1
            n = converter(n)
    print("Case #%d: "%case,end="")
    print(n)
    case += 1
