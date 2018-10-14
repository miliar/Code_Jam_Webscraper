
f = open('C.in')
lines = f.read().splitlines()
f.close()

T = int(lines.pop(0))

result = []

for i in xrange(T):
    line = lines.pop(0)
    R,k,N = [int(x) for x in line.split()]
    
    line = lines.pop(0)
    groups = [int(x) for x in line.split()]
    
    total = 0
    subtotal = 0
    #print "We have", groups
    r = 0
    index = 0
    while r < R:
        subtotal = 0
        start = index
        while (subtotal + groups[index] <= k): #check cycle with index==start
            subtotal+= groups[index]
            index+=1
            index%= N
            if index == start:
                break;
                
        r+=1
        total+=subtotal
        #print "After repetition",r,"we have",subtotal,total,"index is at", index
    #print
    
    result.append('Case #%d: %d' % (i+1, total))

result = '\n'.join(result)
f=open('C.out','w')
f.write(result+'\n')
f.close()
print result

