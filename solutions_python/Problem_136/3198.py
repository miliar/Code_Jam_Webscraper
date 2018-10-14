
fi = open('input', 'r')


no_test_cases = int(fi.readline())


def solve ( c ,f  , x ,rate):
    time  = 0
    while  ( x - c) * f /c > rate:
        #print "Rate: " , rate
        #print "Max: " , ( x - c) * f /c
        
        time += c/ rate
        rate = rate+f
    time = time + x / rate
    return time
    
for i in range( 0 , no_test_cases):
    inp = map( float , fi.readline().split())
    c , f ,x = inp
    rate = 2
    print "Case #" + str(i+1) +": ",
    print solve( c , f ,x , rate)
    
    
