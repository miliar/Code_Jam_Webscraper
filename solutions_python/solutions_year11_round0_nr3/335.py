filename = 'C-large'

fin = open(filename + '.in', 'r')
out = open(filename + '.out', 'w')

T = int( fin.readline() )

for t in range(1, T+1):
    
    N = int(fin.readline())
    
    candies =  map(lambda x: int(x), fin.readline().split(' '))
    
    min = candies[0]
    
    sum = 0
    xsum = 0
    
    for c in candies:
        if min > c:
            min = c
            
        sum += c
        
        xsum = xsum ^ c
    
    
    if xsum == 0:
        out.write("Case #%d: %d\n" % (t, sum-min))
    else:
        out.write("Case #%d: NO\n" % t)


fin.close()
out.close()