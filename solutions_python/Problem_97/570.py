from sys import stdin

def process():
    stdin.readline() #omit the input len
    for lno,line in enumerate(stdin):
        _in = line.split()
        digit = len(_in[0])
        A,B = int(_in[0]),int(_in[1])
        count = 0
        for n in xrange(A,B+1):
            nstr = str(n)
            used = set()
            for i in xrange(1,digit):
                if nstr[i] < nstr[0]: continue
                m = int(nstr[i:]+nstr[:i])
                if m <= B and m > n:
                    if m in used:
                        continue
                    used.add(m)
                    count += 1
        print "Case #%d: %d"% (lno+1,count)
        
if __name__=="__main__":
    process()
