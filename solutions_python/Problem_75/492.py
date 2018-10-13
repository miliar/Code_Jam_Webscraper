import sys

pairs = {}
oppose = {}

def do_magika(s,ctr):
    l = build_maps(s)
    print "Case #%s: [%s]" % (ctr,", ".join(l))
    #print s

def do_magik(s):
    l = []
    for c in s:
        l.append(c)
        if len(l) >= 2:
            last = l[-1]
            slast = l[-2]
            if pairs.has_key((last,slast)):
                l.pop()
                l.pop()
                v = pairs[(last,slast)]
                l.append(v)
            elif pairs.has_key((slast,last)):
                l.pop()
                l.pop()
                v = pairs[(slast,last)]
                l.append(v)

            last = l[-1]
            if len(l) >= 2:
                for i in range(0,len(l)-1):
                    if oppose.has_key((l[i],last)):
                        l = []
                        break
                    elif oppose.has_key((last,l[i])):
                        l = []
                        break
    return l


def build_maps(s):
    pairs.clear()
    oppose.clear()
    parts = s.split()
    np = int(parts[0])
    no = int(parts[np+1])
    string = parts[-1]
    #print np,no,string
    if np > 0:
        for i in range(1,np+1):
            v = parts[i]
            #print v
            pairs[(v[0],v[1])] = v[2]
            pairs[(v[1],v[0])] = v[2]
    if no > 0:
        for i in range(np+2,np+2+no):
            v = parts[i]
            #print v
            oppose[(v[0],v[1])] = ''
            oppose[(v[1],v[0])] = ''
    return do_magik(string)

if __name__ == "__main__":
    f = open(sys.argv[1])
    n = int(f.readline())
    for i in range(0,n):
        s = f.readline().strip()
        do_magika(s,i+1)
    f.close()
