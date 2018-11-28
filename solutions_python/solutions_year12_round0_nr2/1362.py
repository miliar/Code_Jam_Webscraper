import sys

n = sys.stdin.readline()

rawdata=sys.stdin.readline()
i = 1
scores = []
string = ""
for g in rawdata:
    if (g == "\n"):
        scores.append(string)
        string = ""
    else:
        string = string + g
i = 1
for s in scores:
    sList = s.split()
    N = sList[0]
    sups = int(sList[1])
    p = int(sList[2])
    t = sList[3:]
    tprime = list(t)
    t = []
    for t1 in tprime:
        t.append(int(t1))
    t.sort()
    t.reverse()
    issup = False
    numsup = 0
    total = 0
    for t1 in t:
        if (((t1+4)/3) < p):
            break
        if (t1 < p):
            break
        if (not issup):
            if (((t1 + 2)/3) >= p):
                total = total + 1
            else:
                issup = True
        if ((issup) and (numsup < sups)):
            if(((t1 + 4)/3) >= p):
                total = total + 1
                numsup = numsup + 1
            else:
                break
    print("Case #" + str(i) + ": " + str(total))
    i = i + 1
    
     
