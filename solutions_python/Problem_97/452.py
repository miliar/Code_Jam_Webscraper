inp = open("input.txt")
out = open("output.txt","w")
inp.readline()
for k,line in enumerate(inp):
    pairs = set()
    a,b = map(int, line.split(" "))
    for i in range(a,b+1):
        s = str(i)
        for j in range(1,len(s)):
            tmp = s[j:]+s[0:j]
            if (tmp[0] != '0'):
                tmp = int(tmp)
                if (tmp<=b and tmp>i):
                    pairs.add((i,tmp))
    out.write("Case #%i: %i\n" % (k+1,len(pairs)))
out.close()
