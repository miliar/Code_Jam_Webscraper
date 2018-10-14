#This code is for small input only For 1<=A<=B<=1000


import math

cases = int(raw_input())

for x in xrange(cases):
    #read in content
    a, b = map(int, raw_input().split())


    #code
    c = int(math.sqrt(a))
    d = int(math.sqrt(b))

    count = 0

    while c<=d:
        c1 = c**2
        

        s1 = str(c)
        

        if c1>=a and c1<=b and s1 == s1[::-1]:
            s2 = str(c1)
            if s2 == s2[::-1]:
                count+=1

        c+=1

    #code ends

    
    #Output
    print "Case #%d: %d" %(x+1,count)
