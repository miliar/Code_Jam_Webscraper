from math import pow

length = int(raw_input())
for i in xrange(length):
#    print
    tmp = map(int,raw_input().split())
    snappers = tmp[0]
    clicks = tmp[1]        
    total = (snappers-1)*2+1

    counter = pow(2,snappers)
    
    valid  = False
    valid = counter != 0
    if(valid):
        valid = (clicks+1)%(counter) == 0
    if(valid):           
        print "Case #%d: ON"%(i+1)
    else:
        print "Case #%d: OFF"%(i+1)