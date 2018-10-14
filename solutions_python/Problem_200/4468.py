def tidy(n):
    n = str(n)
    c = 1
    for i in range(len(n)-1):
        if int(n[i]) <= int(n[i+1]):
            c+=1
    if c == len(n):
        return True
    else:
        return False

def lastTidy(n):
    for i in range(n,0,-1):
        if tidy(i) == True:
            return i
    return "sww..."

t = int(input())

for i in range(t):
    n = int(input())
    print("Case #"+str(i+1)+": "+" "+str(lastTidy(n)))
