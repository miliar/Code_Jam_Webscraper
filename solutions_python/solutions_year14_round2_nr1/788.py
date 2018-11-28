import sys

def check(lat,n):
    gold = lat[0][0] 
    for i in range(n):
        if lat[i][0] != gold:
            return 'Fegla Won'
    edits = 0
    for j in range(len(gold)):
        nsum = 0
        for i in range(n):
            nsum += lat[i][1][j]
        avg = nsum/n
        for i in range(n):    
            edits += abs(lat[i][1][j]-avg)
    return edits
	#transform data

def transform(val):
    prev = val[0]
    outputstr = ''
    outputval = []
    
    ncount = 0
    while True:
        l = val[0]
        val = val[1:]
        if l == prev:
            ncount +=1
        else:
            outputstr+= prev
            outputval.append(ncount)
            prev = l
            ncount = 1
        if len(val) == 0:
            #output.append([prev,ncount])
            outputstr+= prev
            outputval.append(ncount)
            break
    return [outputstr, outputval]

if __name__ == "__main__":
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)

    t = int(f.readline())
    for _t in xrange(t):
        g = int(f.readline())
        lat  = [[]]*g
        for _u in xrange(g):
            gak = f.readline().split()[0]
            lat[_u] = transform(gak)
        print "Case #" + str(_t+1) + ": " + str(check(lat,g))
                
            #        print lat
        #        check(lat)

