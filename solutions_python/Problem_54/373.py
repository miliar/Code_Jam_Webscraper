def gcd( a, b ):
    if b == 0:
        return a
    else:
        return gcd( b, a % b )
        
        
def gcd_list( z ):
    if len(z) == 1:
        return z[0]
    elif len(z) == 2:
        return gcd( z[0], z[1] )
        
    return gcd( z[0], gcd_list( z[1:] ) )



n = int(raw_input())

for kase in range(1, n+1):
    line = raw_input().split()
    events = int(line[0])
    eventtimestr = line[1:]
    eventtimes=[]
    for j in eventtimestr:
        eventtimes = eventtimes + [long( j )]
        
    # find the differences
    differences = []
    for i in range( 0, len(eventtimes) ):
        for j in eventtimes[i+1:]:
            differences = differences + [ abs(eventtimes[i] - j) ]
            
    gcddiffs = gcd_list( differences )
    
    print ''.join(["Case #", str(kase), ": ", str((((eventtimes[0]/gcddiffs)+1)*gcddiffs-eventtimes[0])%gcddiffs)])