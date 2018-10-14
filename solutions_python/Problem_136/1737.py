import math
def solve2(c,f,x,i):
    rate=2
    t=0
    while i>0:
        t=t+float(c)/float(rate)
        rate = rate + f
        i =i -1
    t = t+ float(x)/float(rate)
    return t
def solve(c,f,x):
    n = int(math.floor(x/c))
    answers={}
    for i in range(0,n+1):
        answers[i]=solve2(c,f,x,i)
    minva=min(answers.values())
    return minva
fuck=0
for line in open("a.txt","r").readlines():
    fuck=fuck+1
    c=float(line.split(" ")[0])
    f=float(line.split(" ")[1])
    x=float(line.split(" ")[2])
    minva=solve(c,f,x)
    open("b.txt","a").write(u"\nCase #%d: " % fuck +str(minva))
