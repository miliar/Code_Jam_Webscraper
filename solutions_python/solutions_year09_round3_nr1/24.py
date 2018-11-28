import sys, itertools

with open(sys.argv[1]) as f:
    for n in range(int(f.readline().strip())):
        inp = list(f.readline().strip())
        rule = {}
        rule[inp[0]]=1
        first = True
        c = itertools.count(2)
        for z in inp:
            if z not in rule:
                if first:
                    rule[z] = 0
                    first = False
                else:
                    rule[z] = c.__next__() 
        b = c.__next__()
        minnum = 0
        pni = list(reversed(inp))
        for i in range(len(pni)):
            minnum += rule[pni[i]] * b ** i

        print("Case #",str(n+1),": ",minnum,sep="")

