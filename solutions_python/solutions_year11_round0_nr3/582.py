import re,sys,itertools

numCases = int(sys.stdin.readline())

cases = []

def binadd(x,y):
    x = bin(x)[2:]
    y = bin(y)[2:]
    c = max(len(x),len(y))
    if c == len(y):
        for i in range(c - len(x)):
            x = "0" + x
    else:
        for i in range(c - len(y)):
            y = "0" + y
    answer = ""
    for n in range(c):
        if x[n] is '1' and y[n] is '1':
            answer = answer + "0"
        else:
            answer = answer + str(int(x[n]) + int(y[n]))
    return int(answer,2)

def equalPiles(p1,p2):
    p1total = 0
    p2total = 0
    actualtotal = 0
    for candy in p1:
        p1total = binadd(p1total,int(candy))
        actualtotal += int(candy)
    for candy in p2:
        p2total = binadd(p2total,int(candy))
    
    if p1total == p2total:
        return actualtotal
    else:
        return 0

def bestPile(N,pile):
    best = 0
    for size in range(1,N/2+1):
        combo = itertools.combinations(pile,size)
        for item in combo:
            hold = []
            hold2 = []
            hold.extend(pile)
            for num in item:
                hold.remove(num)
                hold2.append(num)
            
            a = equalPiles(hold,hold2)
            
            best = max(a,best)
    
    if best > 0:
        return str(best)
    else:
        return "NO"

for n in range(numCases):
    cases.append(re.split(r'\s+',sys.stdin.readline().strip() + " " + sys.stdin.readline().strip()))

k = 1
for case in cases:
    N = int(case[0])
    case = case[1:]
    print "Case #" + str(k) + ": " + str(bestPile(N,case))
    k = k + 1
