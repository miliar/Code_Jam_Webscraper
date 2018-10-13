#!/usr/bin/env python

infile = "A-large.in"
#infile = "A-small-attempt5.in"
#infile = "A-sample.in"
outfile = infile.split(".")[0] + ".out"

def exists(expath, path):
    l = len(path)
    for item in expath:
        if path == item[:l] and (len(item) == l or item[l] == '/'): return True
    return False


fsrc = open(infile, "r")
fres = open(outfile, "w")

T = int(fsrc.readline())

for t in range(T):
    N, M = [int(value) for value in fsrc.readline().split()]
    expath = []
    for i in range(N):
        expath.append(fsrc.readline().strip())
    inpath = []
    for i in range(M):
        inpath.append(fsrc.readline().strip())
    
    print expath
    print inpath

    count = 0
    for path in inpath:
        temp = path[:]
        while temp != '' and not exists(expath, temp):
            temp = temp[:temp.rfind('/')]
            count += 1
        expath.append(path[:])
    
    
    
    
    res = "Case #%s: %s" %(t+1, count) 
    
    
    res += '\n'
    print res,
    fres.write(res)
    #raw_input('')

fsrc.close()
fres.close()
