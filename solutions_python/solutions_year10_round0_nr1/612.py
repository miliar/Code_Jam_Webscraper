file = open("A-large.in.in","r")

t=int(file.readline())

def int2bin(n, count=24):
    return "".join([str((n >> y) & 1) for y in range(count-1, -1, -1)])

for i in range(t):
    nk = file.readline().split(" ")
    n = int(nk[0])
    k = int(nk[1])
    
    left = k % (2**n)
    
    s =  int2bin(left,count=n)
    
    if s.find('0') == -1:
        print "Case #%d: ON" % (i+1)
    else:
        print "Case #%d: OFF" % (i+1)
        
file.close()