# -*- coding: latin-1 -*- 

try:
    file = open("a.in", "r")
    lines = int(file.readline())
    out = open("a.out", "w")
    
    for i in range(lines):
        tmp = (file.readline()).split()
        N = int(tmp[0])
        K = int(tmp[1])
        
        if (K & ((1 << N)-1)) == ((1 << N)-1):
            out.write("Case #" + str(i+1) + ": ON\n")
        else: out.write("Case #" + str(i+1) + ": OFF\n")
    
    file.close()
    out.close()
except IOError:
    print "IOError!"
