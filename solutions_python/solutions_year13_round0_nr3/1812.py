from math import sqrt

def isPal(n):
    return str(n)==str(n)[::-1]


max = 10**14
n = 1
fsq = []
while n**2<=(max):
    if isPal(n) and isPal(n**2):
        fsq.append(n**2)
    n+=1

with open('C-large-1.in') as f:
    lines = f.readlines()
tcases = int(lines[0])

with open('output.txt','w') as f:
    for case in range(0,tcases):
        line = lines[case+1]
        lower, upper = map(int,line.split(" "))
        total = 0
        for a in fsq:
            if lower<=a<=upper:
                total+=1
        f.write("Case #" + str(case+1) + ": " + str(total) + '\n')