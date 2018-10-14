"""
def legit(i):
    x = str(i)
    for j in range(1,len(x)):
        if x[j] < x[j-1]:
            return False
    return True
"""
    
T = input()

for case in xrange(1,T+1):
    n = raw_input()
    
    if len(n) == 1:
        ans = n
    else:
        for i in range(1,len(n)):
            if n[i] < n[i-1]:

                for j in range(i-1,0,-1):
                    if n[j] != n[j-1]: # j ~ i-1 all -1
                        break
                    
                else: # all 1's from start? -1 digit
                    if n[0] == '1':
                        ans = '9' * (len(n)-1)
    
                    else:
                        ans =  str(int(n[0])-1) +'9' * (len(n)-1)
                    break

                d = str(int(n[j])-1)
                
                ans = n[:j] + d * (i-j) + '9'*(len(n) - i)


                break
        else:
            ans = n # already ordered
                
        
    """
        
    x = int(n)
    
    for i in range(x,0,-1):
        if legit(i):
            break

    if i != int(ans):
        print i,ans,n
    """  

    print "Case #%d: %s" % (case,ans)

