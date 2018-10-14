from sys import stdin
t = int(stdin.readline())
counter = 0
D = {}
mini, maxi = 100000, 2000000
for i in range(mini, maxi + 1):
    l = len(str(i))
    s = str(i) * 2
    for x in range(1, l):
        tok = s[x:l + x]
        n, m = i, int(tok)
        if n < m and n >= mini and n <= maxi and m >= mini and m <=  maxi:
            try:
                D[n].add(m)
            except KeyError:
                D[n] = set([])
                D[n].add(m)

for case in range(1, t + 1):
    total = 0
    a, b = stdin.readline().split()
    mini, maxi = int(a), int(b)
    if maxi < 100000:
        d = set([])
        for i in range(mini, maxi + 1):
            l = len(str(i))
            s = str(i) * 2
            for x in range(0, l - 1):
                tok1 = s[x:l + x]
                for y in range(x+1, l):
                    tok2 = s[y:l + y]
                    n, m = (int(tok1), int(tok2))
                    #print n,m
                    if n < m and (n,m) not in d and n >= mini and n <= maxi and m >= mini and m <=  maxi:
                        d.add((n, m))
        total = len(d)
    else: 
        for n in range(mini, maxi + 1):
            count = 0
            try:
                for m in D[n]:
                    if m <= maxi:
                        count += 1
                total += count 
            except KeyError:
                pass
    print "Case #%d: %d" %(case, total,)
