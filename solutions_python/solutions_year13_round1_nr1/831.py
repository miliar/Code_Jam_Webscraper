'''
Created on 27-Apr-2013

@author: Bijil
'''

t=int(raw_input(''));
case_sol=[];

for k in range(t):
    rl=(raw_input()).split(' ')
    r=int(rl[0])
    l=int(rl[1])
    r1=r
    used=0
    count=0
    pred_used=0
    
    while 1:
        tmp_used=((r1+1)*(r1+1))-(r1*r1)
        pred_used+=tmp_used
        #print str(tmp_used)+" "+str(pred_used)+" "+str(l)
        if(pred_used>l):
            break
        used=pred_used
        r1=r1+2
        count=count+1
        
    case_sol.append(count)

f = open('1a.txt','w')    
for j in range(t):

    f.write('Case #'+str(j+1)+': '+str(case_sol[j])+"\n")
    print 'Case #'+str(j+1)+': '+str(case_sol[j]) 