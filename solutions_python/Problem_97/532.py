f = open('C-small-attempt0.in.txt', 'r')
f1 = open('C-small-attempt0.out.txt', 'w')
t = int(f.readline())
inp = []
res = []
cas=1
for y in range(t):
    cur = []
    a = f.readline().split()
    num1,num2=int(a[0]),int(a[1])
    for num in range(num1, num2+1):
        ndigits = len(str(num2))
        if ndigits <= 1:
            break
        for n in range(ndigits):
            curn = int(str(num)[-n:] + str(num)[:-n])
            if curn >= num1 and curn < num2 and curn < num:
                if cur.count((curn, num)) < 1:
                    cur.append((curn, num))
    f1.write('Case #%d: %d\n' % (cas, len(cur)))
    cas+=1