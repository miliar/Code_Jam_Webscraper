        
f = open('ip.txt', 'r')
g = open('op.txt', 'w')
for line in f:
    t = int(line)
    break

x = 0
for line in f:
    s,k = line.split()
    k = int(k)
    n = len(s)
    count = 0
    a = []
    for e in s:
        if (e == '-'):
            a.append(1)
        else:
            a.append(0)
    i = 0
    while (i <= n-k):
        while (i < n and a[i] == 0):
            i+=1
        if (i > n-k):
            break
        for j in range(k):
            a[j+i] = 1 - a[j+i]
        count += 1
    while (i < n):
        if (a[i] == 1):
            count = -1
        i+=1
    if (count == -1):
        g.write("Case #"+str(x+1)+": IMPOSSIBLE\n")
    else:
        g.write("Case #"+str(x+1)+": "+str(count)+"\n")
    x += 1

f.close()
g.close()
print 'done'
