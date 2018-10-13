T = int(raw_input())

for t in range(1,T+1):
    smax, shyness = raw_input().split()
    
    people = 0
    asked = 0

    for i in range(int(smax) + 1):
        shy = int(shyness[i])
        
        if people < i and shy > 0:
            asked += i - people
            people += asked
        
        people += shy
        
    print "Case #%d: %d" % (t, asked)
