import sys

sys.setrecursionlimit(1000000)

f = open(sys.argv[1]) if len(sys.argv)>1 else sys.stdin

total = int(f.readline().strip())

def input():
    l = f.readline().strip()
    letter = []
    count = []
    for s in l:
        if not letter or s != letter[-1]:
            letter.append(s)
            count.append(1)
        else:
            count[-1] += 1
    return (letter, count) 

for i in range(total):
    sys.stdout.write("Case #%d: " % int(i+1))
    n = int(f.readline().strip())
    ls = []
    ns = []
    for j in range(n):
        x, y = input()
        ls.append(x)
        ns.append(y)
    x = ls[0]
    fwin = False
    for j in range(n):
        if x!= ls[j]:
            fwin = True
    if fwin:
        print("Fegla Won")
        continue
    lc = len(ls[0])
    result = 0
    for j in range(lc):
        s = 0
        for k in range(n):
            s += ns[k][j]
        avg = round(s/n)
        for k in range(n):
            result += abs(avg - ns[k][j])
    print(result) 
