done = False
front = True
repeat = False
def checkD(n,k):
    check = True
    if(len(n) != k):
        check = False
    for a in n:
        if(a == "+"):
            check = False
    return check
def fromFront(p):
    global n
    global k
    global front
    global repeat
    for b in range(len(n)-k+1):
        if(repeat == False):
            if(n[b] == "-"):
                for c in range(k):
                    if(n[b+c] == "-"):
                        n[b+c] = "+"
                    else:
                        n[b+c] = "-"
                repeat = True
            if(b == (len(n)-k)):
                front = False
    if(check(n) == True):
        return str(p)
def fromBack(p):
    global n
    global k
    global front
    global repeat
    for d in range(len(n)-1,k-1,-1):
        if(repeat == False):
            if(n[d] == "-"):
                for c in range(k):
                    if(n[d-c] == "-"):
                        n[d-c] = "+"
                    else:
                        n[d-c] = "-"
                repeat = True
            if(d == k):
                front = True
    if(check(n) == True):
        return str(p)
def check(n):
    c = True
    for a in n:
        if(a == "-"):
            c = False
    return c
def solve():
    global repeat
    global n
    global k
    global front
    if(check(n) == True):
        return "0"
    elif(checkD(n,k) == True):
        return "1"
    else:
        for a in range(1,1000):
            repeat = False
            if(front == True):
                fromFront(a)
            else:
                fromBack(a)
            if(check(n) == True):
                return str(a)
    return "IMPOSSIBLE"
t = int(input())
for i in range(1,t+1):
    done = False
    front = True
    repeat = False
    n, k = [s for s in input().split(" ")]
    n = list(n)
    k = int(k)
    print("Case #{}: {}\n".format(i,solve()))
