#Google Code Jam 2012
#Qualification Round
#Problem B


#Let's create the list of possible scores instead of hand-picking them
sets=[[i,j,k] for i in range(11) for j in range(11) for k in range(11)]
sets=[e for e in sets if e[0]>=e[1]>=e[2] and e[0]-e[2]<=2]
#...split them in two groups
special=[e for e in sets if e[0]-e[2]==2]
nonspecial=[e for e in sets if e[0]-e[2]<2]
#...and create some look up tables
maxspecialscores={sum(e):max(e) for e in special}
def maxSS(n):
    if n in maxspecialscores: return maxspecialscores[n]
    else: return -1

maxnonspecialscores={sum(e):max(e) for e in nonspecial}
def maxNSS(n):
    if n in maxnonspecialscores: return maxnonspecialscores[n]
    else: return -1

def file2gen(name):
    f=open(name,'r')
    text=f.read()
    f.close()
    return (line for line in text.splitlines())

def parse(gen):
    cases=int(next(gen))
    tr=[[]]*cases
    for i in range(cases):
        li=[int(e) for e in next(gen).split()]
        tr[i]=[li[1],li[2],sorted(li[3:],reverse=True)]
    return tr

def answer(case):
    (s,p,li)=case
    total=0
    extras=s
    i=0
    while i<len(li) and maxNSS(li[i])>=p:
        total+=1
        i+=1
    while i<len(li) and maxSS(li[i])>=p and extras>0:
        total+=1
        extras-=1
        i+=1
    return total

def output(filein, fileout):
    cases=parse(file2gen(filein))
    f=open(fileout,'w')
    for i in range(len(cases)):
        f.write('Case #'+str(i+1)+': '+str(answer(cases[i]))+'\n')
    f.close()

if __name__=='__main__': output('B-large.in','out.txt')

    
