from __future__ import division

fi=open('A-small-attempt0.in','r')
fo=open('A-small-attempt0.out','w')

def wp(team):
    s=0
    no=0
    for i in team:
        if i>=0:
            s+=i
            no+=1
    return s/no

def owp(team,tlist):
    no=0
    s=0
    for j in range(len(team)):
        if team[j]>=0:
            no+=1
            temp=[]
            for k in tlist[j]:
                temp.append(k)
            
            if team[j]==1:
                temp.remove(0)
            else:
                temp.remove(1)
        
            s+=wp(temp)
    return s/no

def oowp(team,tlist):
    no=0
    s=0
    for j in range(len(team)):
        if team[j]>=0:
            no+=1
            s+=owp(tlist[j],tlist)
    return s/no

t=int(fi.readline())
for i in range(t):
    fo.write("Case #"+str(i+1)+":\n")
    n=int(fi.readline())
    tlist=[]
    for j in range(n):
        line=fi.readline().strip()
        team=[]
        
        for elem in line:
            if elem=='1' or elem=='0':
                team.append(int(elem))
            else: 
                team.append(-1)
        tlist.append(team)
   
    for team in tlist:
        
        fo.write(str(0.25 * wp(team) + 0.50 * owp(team,tlist) + 0.25 * oowp(team,tlist))+"\n")
        
fo.close()
fi.close()
                
        