import math
import operator
import re
def test(x,i):
    return (sum(x)==i,max(x)-min(x))
ps=[]

def gen(i):
    res=[i]
    if (i-5)%3==0:
        t=sorted([i/3 + 1, i/3, i -2*i/3])        
    else:
        t=sorted([i/3, i/3, i -2*i/3])    
    res.append(t)
    if i<29 and i>1:
        s1=sorted([max(t)+1,min(t),max(t)-1])
        s2=sorted([max(t),min(t)-1,min(t)+1])
        if test(s1,i)[0] :
            res.append(s1)
        elif test(s2,i)[0]:
            res.append(s2)
    return res
fname='B-small-attempt1.in'
fin=open(fname)
fout=open(fname+".out.txt", "w")
T = int(fin.readline().strip())
for ti in range(T):
    splitter = re.compile(r'[\D]') # Match non-digits
    score_list = map(int,splitter.split(fin.readline().strip()))
    n=score_list.pop(0)
    s=score_list.pop(0) #number of surpising
    p=score_list.pop(0) #best result
    
    #print "n", n,"s", s,"p", p
    res=[]
    for si,score in  enumerate(score_list):
        pscore=gen(score)
        #print pscore
        norm=False
        for score in pscore[1]:
            if score>=p:
                norm=True;  break            
        su=False
        if len(pscore)==3: #there is surprising
            for score in pscore[2]:
                if score>=p:
                    su=True; break
        res.append([norm,su])
    answer=0
    #print 's onlys' 
    for i,r in enumerate(res):
        #print i, r
        if s>0:
            if not(r[0]) and r[1]:
                #print i, r
                answer+=1;
                s-=1;
                res.pop(i)
    #print s, res
    #print 'get rest of possible s'
    for i,r in enumerate(res):
        #print i, r
        if s>0:
            if r[1]:
                #print i, r
                answer+=1;
                s-=1;
                res.pop(i)
    #print s, res
    'get all normal remaining'
    for i,r in enumerate(res):
        #print i, r
        if r[0]:
            #print i, r
            answer+=1  
    #print("Case #{0}: {1}\n".format(ti+1, answer ))
    fout.write("Case #{0}: {1}\n".format(ti+1, answer ))
fin.close()
fout.close()
