stri = raw_input()
z = int(stri)

for t in range(z):

    n = (raw_input())
    
    if(len(n)<2):
        print "Case #" + str(t+1) + ": " + str(n)
        continue

    maxpos = 0
    pos = -1
    result = n
    for i in range(0, len(n)):
        if(int(n[i]) > int(n[maxpos])):
            maxpos = i;
            
        if(i + 1 < len(n)):
            if (n[i] > n[i+1]):
                pos = maxpos
                break
    
    if(pos >= 0):
        result = (n[0:pos] if (pos-1>=0) else "") + str( int( n[pos] ) - 1 ) + '9'*(len(n)-pos-1)
    
    print "Case #" + str(t+1) + ": " + str(int(result))