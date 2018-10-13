
n = 0
t = 0
seq = []

fp = open("large.in")  #input filename
fout = open("out_large.txt", "w") #output filename

def get_input():
    global n, t, seq, oseq, bseq
    n = int(fp.readline())
    
    for i in xrange(n):
        seq = []
        oseq = []
        bseq = []
        line = fp.readline().split()
        t = int(line[0])
        for j in xrange(1, t+1):
            rob = line[j * 2 - 1]
            pos = int(line[j*2])
            seq.append((rob, pos))
        yield

def process():
    r=0
    o_time_taken = 0
    b_time_taken = 0
    bpos = 1
    opos = 1
    
    for i in xrange(t):
        if seq[i][0] == 'B':
            dis = abs(seq[i][1] - bpos)
            dis = dis - o_time_taken
            if dis < 0:
                dis = 0
                
            bpos = seq[i][1]
            o_time_taken = 0
            b_time_taken += dis + 1
        else:
            dis = abs(seq[i][1] - opos)
            dis = dis - b_time_taken
            if dis < 0:
                dis = 0

            opos = seq[i][1]
            b_time_taken = 0
            o_time_taken += dis + 1

        r += (dis + 1)            
    return r
    
for i,j in enumerate(get_input(), 1):
    #print n,t, seq, i
    r = process()
    #print "Case #%s: %s" % (i, r)
    print >> fout, "Case #%s: %s" % (i, r)

fout.close()
