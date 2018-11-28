
t = 0
fp = open("small.in")  #input filename
fout = open("small_out.txt", "w") #output filename

def get_input():
    global t

    t = int(fp.readline())
    
    for i in xrange(t):
        oseq = {}
        cseq = {}
        seq = ""
        seq = []
        line = fp.readline().split()
        c = int(line[0])
        if c:
            for celem in line[1: c+1]:
                cseq[celem[0] + celem[1]] = celem[2]
                cseq[celem[1] + celem[0]] = celem[2]
        
        d = int(line[1+c])
        if d:
            for oelem in line[1+c+1 : 1+c+1+d]:
                oseq[oelem[0]] = oelem[1]
                oseq[oelem[1]] = oelem[0]
        n = int(line [1+c+1+d])
        seq = line [1+c+1+d+1]
        yield c,cseq, d,oseq, n, seq

def process(c,cseq, d, oseq, n, seq):
    r= [seq[0]]
    last = seq[0]
    for s in seq[1:]:
        if (s + last) in cseq:
            r.pop()
            r.append(cseq [s+last])
            last = cseq [s+last]
        elif s in oseq and oseq[s] in r:
            r = []
            last = ''
        else:
            r.append(s)
            last = s
        
    return r
    
for i,j in enumerate(get_input(), 1):
    #print n,t, seq, i, cseq, oseq
    c, cseq, d,oseq, n, seq = j
    r = process(c,cseq, d, oseq, n, seq)
    #print "Case #%s: [%s]" % (i, ', '.join(r))
    print >> fout, "Case #%s: [%s]" % (i, ', '.join(r))
#print n,t, seq, i, cseq, oseq
fout.close()
