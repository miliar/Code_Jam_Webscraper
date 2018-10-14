def doit(n):
    s = list(set(n))
    l = len(n)
    ndict = dict( (entry, None) for entry in s)
    ndict[n[0]] = 1
    res = 0
    nlst = range(len(s))
    if len(s) == 1:
        res = 2 ** l - 1
    else:
        nlst.pop(1)
        #print nlst 
        for c in n:
            if ndict[c] == None:
                ndict[c] = nlst.pop(0)
            res = res + len(s) ** (l - 1) * ndict[c]
            l -= 1
            #print c, res, ndict[c]
    return res

fd = open("A-large.in.txt")
t = int(fd.readline())
for i in xrange(t):
    line = fd.readline()
    if line.endswith("\n"):
        line = line[:-1]
    print "Case #%d: %d" %(i+1, doit(line))
    

#print doit("11001001")
#print doit("cats")
#print doit("zig")
                        
            
