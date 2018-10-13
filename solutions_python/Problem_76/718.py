f = open("C-small-attempt3.in","r")
f2 = open("C.out","w")

def solve(c):
    n = len(c)
    bucket = [[],[]]
    out = "NO"
    
    shift = 2**(n-1)
    for num in xrange(1, 2 ** (n-1) ):
        bucket = [[],[]]
        selection = [0] + map(int, list(bin(shift + num)[2:]))[1:]
        #print selection
        for idx, item in enumerate(selection):
            bucket[item].append(c[idx])
        
        x1,x2=0,0
        for i in bucket[0]:
            x1 = x1 ^ i
        for i in bucket[1]:
            x2 = x2 ^ i
        if ( x1 == x2 ):
            #print bucket[0], bucket[1]
            if out == "NO":
                out = 0
            
            out = max( out, sum(bucket[0]), sum(bucket[1]))
            

    return out

for idx in xrange(int(f.readline().strip())):
    n = int(f.readline().strip())
    cs = map(int,f.readline().strip().split())
    out = "NO"
    out = solve(cs)
    f2.write( "Case #%d: " % (idx+1) )
    f2.write( str(out))
    f2.write( "\n" )


f2.close()

f.close()
