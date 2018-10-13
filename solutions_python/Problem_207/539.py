from itertools import permutations
list3=['RR','BB','YY']
t=int(raw_input(''))
for a0 in xrange(t):
    q=raw_input('')
    
    list1= map(int, q.split())
    
    n=list1[0]
    r=list1[1]
    o=list1[2]
    y=list1[3]
    g=list1[4]
    b=list1[5]
    v=list1[6]
    ans=''
    perms=[]
    for i in xrange(r):
        ans=ans+'R'
    for i in xrange(y):
        ans=ans+'Y'
    for i in xrange(b):
        ans=ans+'B'
    perms = [''.join(p) for p in permutations(ans)]
    k=0
    ends=''
    for i in xrange(len(perms)):
        k=0
        ends=''
        if list3[0] in perms[i]:
            fin='IMPOSSIBLE'
            k=1
        if list3[1] in perms[i]:
            fin='IMPOSSIBLE'
            k=1
        if list3[2] in perms[i]:
            fin='IMPOSSIBLE'
            k=1
        ends=ends+perms[i][0]
        ends=ends+perms[i][n-1]
        if ends in list3:
            fin='IMPOSSIBLE'
            k=1

        
        if k==0:
            print "Case #"+str(int(a0+1))+":",perms[i]
            break
        if k==1 and i==len(perms)-1:
            print "Case #"+str(int(a0+1))+":",fin
            
        


       
                    
    
            

                    
                
    









    
        
