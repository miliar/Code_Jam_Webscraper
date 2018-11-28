import sys
fp = file(sys.argv[1])
t = fp.next()
c = []
for i in range(int(t)):
    n, m = fp.next().split()
    n = int(n) #s_max
    l = [int(ch) for ch in m] #list
    #count the number of people exists already
    c_people, ctr = 0, 0
    for j in range(len(l)):   
        if c_people < j: #if
            ctr += j - c_people       #add the req people. ctr = 0, 
            c_people += j - c_people
        c_people += l[j]  #cp = 1, 
    c.append(ctr)
    
for i in range(int(t)):
    print "Case #%d: %d" %(i+1, c[i])
    
        
    
    