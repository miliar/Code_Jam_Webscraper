import sys

def recycles(line):
    l = line.split()
    A = l[0]
    B = l[1]
    d = len(A)
    res = 0
    for n in xrange(int(A),int(B)+1):
        d = len(str(n))
        if d == 2:
            m = int(str(n)[1]+str(n)[0])
            if len(str(m))==2 and m<=int(B) and m>=int(A) and m!=n:
                res+=1
        elif d == 3:
            m = int(str(n)[1]+str(n)[2]+str(n)[0])
            z = int(str(n)[2]+str(n)[0]+str(n)[1])
            if len(str(m))==3 and m<=int(B) and m>=int(A) and m!=n:
                res+=1
            if len(str(z))==3 and z<=int(B) and z>=int(A) and z!=n:
                res+=1
        else:
            pass
    return res

def process(i, fin, fout):
    line = fin.readline().strip()
    res = recycles(line)
    fout.write("Case #%d: %s\n" % (i+1, res/2))
    
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print "Please indicate input and output"
    fin = open(sys.argv[1], 'r')
    fout = open(sys.argv[2], 'w')
    N = int(fin.readline())
    for i in xrange(N):
        process(i, fin, fout)
    fin.close()
    fout.close()
    print " *** Done ***"