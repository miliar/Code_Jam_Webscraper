# your code goes here

mem = []

def flappable(c, i, a):
    while True:
        ok = True
        for b in range(len(c)):
            if (c[b] != '+'):
                ok = False
        if ok: return a
        if (i > len(c)):
            return -1

        if c[0] == '-':
            for y in range(i):
                c[y] = '+' if c[y] == '-' else '-'
            a = a+1
        c = c[1:]
	
x = int(input())
for i in range(x):
    a = input().split()
    y = a[0]
    z = a[1]
    q = flappable(list(y), int(z), 0)
    q = "IMPOSSIBLE" if q == -1 else q
    print("Case #"+str(i+1)+": "+str(q))

