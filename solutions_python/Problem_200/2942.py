
# coding: utf-8

# In[25]:

n = int(raw_input())
for i in range(n):
    r = [int(u) for u in raw_input()]
    if len(r) == 1:
        print "Case #" + str(i+1) + ":",
        print r[0]
        continue
    #r.reverse()
    changed = True
    while changed:
        changed = False
        for j in range(len(r) - 1):
            #print j, r
            if r[j] > r[j+1]:            
                r[j] -= 1
                #print 'change ', j, ' to ', r[j]
                for a in range(j+1, len(r)):
                    r[a] = 9
                changed = True
                break
            
            #print 'change ', j+1, ' to ', r[j+1]
    #r.reverse()
    
    print "Case #" + str(i+1) + ":",
    print ''.join([str(o) for o in r if o != 0])
    
        

    


# 

# In[ ]:



