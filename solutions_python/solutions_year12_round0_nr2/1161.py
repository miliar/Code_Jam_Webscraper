fob = open('c:/test/b.txt','r')
test = fob.readline()
test = int(test)

i = 0
while i < test:
    line = fob.readline()
    line = line.split()
    n = line[0]
    n = int(n)
    s = line[1]
    s = int(s)
    p = line[2]
    p = int(p)
    t = []
    total = 0

    j = 3
    while j < len(line):
        t.append(int(line[j]))
        j += 1

    k = 0
    while k < len(t):
        if p>=2:
            if t[k]-p-(p-1) > p-2:
                total += 1
            elif t[k]-p-(p-1) == p-2 and s >= 1:
                total += 1
                s -= 1
            elif t[k]-p-(p-2) == p-2 and s >= 1:
                total += 1
                s -= 1
        elif p==1:
            if t[k] >= 1:
                total += 1
        elif p==0:
            total += 1
        k += 1
    print 'Case #'+`i+1`+': '+`total`
    i += 1
fob.close()
