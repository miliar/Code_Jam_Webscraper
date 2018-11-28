ifile = 'A-small-attempt0.in'
ofile = 'A-small-attempt0.out'

ifptr = open(ifile)
ofptr = open(ofile,'w')

gdict = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}

N = int(ifptr.readline().rstrip()) #No. of test cases

for i in range(0,N):
    
    ofptr.write("Case #%d: " % (i+1))
    
    googtxt = list(ifptr.readline())
    
    for c in googtxt:
        
        if c == '\n':
            continue
        
        ofptr.write("%s" % gdict[c])

    ofptr.write("\n")

ifptr.close()
ofptr.close()