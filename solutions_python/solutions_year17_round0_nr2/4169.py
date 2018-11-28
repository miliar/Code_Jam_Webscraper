t = int(raw_input())

for a0 in xrange(t):
    n = map(int , list(raw_input().strip()))
    
    if len(n) > 1:
        if int(''.join(map(str ,n))) < int("1"*len(n)) :
            n = list( "9" * (len(n)-1)) 
        else : 
            index = -1
            streak = 0  
            for i in range(1 , len(n)):
                if n[i-1] > n[i] :
                    index = i - streak - 1
                    break
                elif n[i-1] == n[i] :
                    streak += 1
                else :
                    steak = 0
            
            if index != -1 :
                n[index] = n[index] - 1
            
                for i in range(index+1 , len(n) ):
                    n[i] = 9
        
    print "Case #" + str(a0+1) + ": " + ''.join(map(str ,n))
#    m = []
#    for i in n :
#       m.append(i) 
#    m.sort()
#    if m != n :
#        print a0+1
#        
    
    