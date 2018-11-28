
t = 0
fp = open("large.txt")  #input filename
fout = open("large_out.txt", "w") #output filename

    
def get_input():
    global t

    t = int(fp.readline())
    
    
    for i in xrange(t):
        line = fp.readline()
        n = int(line.strip())
        tab = []
        for j in xrange(n):
            tab.append(fp.readline().strip())
        yield n,tab

def process(n, tab):
    w = [0] * n
    owp = [0] * n
    oowp = [0] * n
     
    tm= [0] * n
    print tab
    for i in xrange(n):
        for  j,ch in enumerate(tab[i]):
            #print 'L',ch
            if ch == '1':
                w[i] += 1
            if ch != '.':
                tm[i] += 1

    for i in xrange(n):
        ow = 0
        owt = 0
        opp = 0
        for j,ch in enumerate(tab[i]):
            
            if ch == '1':
                ow += (w[j] * 1.0/ (tm[j] - 1))
            elif ch == '0':
                ow += ((w[j] -1) * 1.0 / (tm[j] -1))

        owp[i] = ow / tm[i]

    #print "w", w
    #print "t" , tm
    #print "owp ",owp
    rp = []
    for i in xrange(n):
        a=0
        for j, ch in enumerate(tab[i]):
            if ch != '.':
                a += (owp[j] )
        oowp = a/ tm[i]
        #print w[i]*1.0/tm[i], 0.5 * owp[i], 0.25*oowp
        rpi = 0.25 * (w[i] *1.0 / tm[i]) + 0.5 * owp[i] + 0.25 * oowp
        rp.append(rpi)
        
                
    return '\n'.join(map(str,rp))
    
for i,j in enumerate(get_input(), 1):
    n,tab = j
    #print n,tab
    r = process(n,tab)
    print "Case #%s:\n%s" % (i,r)
    print >> fout, "Case #%s:\n%s" % (i,r)
    
fout.close()
