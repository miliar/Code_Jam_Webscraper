import sys

fh = open("A-small-attempt4.in", "r")
fo = open("A-small-attempt4.out", "w")

line = fh.readline()
count = line.strip()
num = 0

for line in fh:
    line = line.strip()
    (nSnappers, nSnaps) = line.split(" ")
    
    nSnappers = int(nSnappers)
    nSnaps = int(nSnaps)
    
    
    S = []
    for i in xrange(nSnappers):
        S.append(0)
        
    for i in xrange(nSnaps):
        
        for m in xrange(nSnappers):
            k = nSnappers - m - 1
            on = True
            for l in xrange(k):
                if S[l] == 0:
                    on = False
            if on:
                if S[k] == 1:
                    S[k] = 0
                else:
                    S[k] = 1
    
    check = True    
    for i in xrange(nSnappers):
        if S[i] == 0:
            check = False
    out = num + 1        
    if check:
        fo.write("Case #" + str(out) + ": ON\n")
    else:
        fo.write("Case #" + str(out) + ": OFF\n")
         
    num += 1
    
    
fh.close()
fo.close()

if __name__ == '__main__':
    pass