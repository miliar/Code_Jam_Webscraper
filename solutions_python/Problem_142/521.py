from __future__ import division
def average(li):
    sum=0
    for i in li :
        sum+=i
    return sum/len(li)

def nearest(average,li):
    mi=99999999
    mi_el=0
    for i in li:
        if abs(average-i)<mi:
            mi=abs(average-i)
            mi_el=i
    return mi_el

def diff(near,li):
    sum=0
    for i in li:
        sum+=abs(i-near)
    return sum
    
def solve(s):
    s_di=[]
    s_ra=[]
    for w in s:
        tmp=""
        prev=""
        ranks=[]
        for i in range(len(w)):
            if w[i]!=prev:
                prev=w[i]
                tmp+=w[i]
                ranks.append(1)
            else:
                ranks[len(ranks)-1]+=1
        s_ra.append(ranks)
        s_di.append(tmp)
    for i in range(len(s_di)-1):
        if s_di[i]!=s_di[i+1]:
            return "Fegla Won"
    moves=0
    for i in range(len(s_ra[0])):
        tmp=[]
        for j in range(len(s_ra)):
            tmp.append(s_ra[j][i])
        avg=average(tmp)
        near=nearest(avg,tmp)
        moves+=diff(near,tmp)
    return moves
        
    
    
    
        
        
        
    
        

fin=open('../in','r') ; fout=open('../out','w')
cases=int(fin.readline().strip())
for case in range(1,cases+1):
    n=int(fin.readline().strip());s=[]
    for i in range(n):
        s.append(fin.readline().strip())
    fout.write("Case #"+str(case)+": "+str(solve(s))+"\n")