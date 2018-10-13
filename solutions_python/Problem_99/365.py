def parse(infile):
    f=open(infile)
    text=f.read()
    f.close()
    return (e for e in text.splitlines())

def file2list(gen):
    cases=int(next(gen))
    tr=[]
    for i in range(cases):
        ab=[int(e) for e in next(gen).split()]
        prob=[float(e) for e in next(gen).split()]
        tr.append([ab,prob])
    return tr

def right(prob):
    p=1
    for i in prob:
        p*=i
    return p

def giveup(case):
    return case[0][1]+2

def keepgoing(case):
    p=right(case[1])
    [a,b]=case[0]
    return p*(b-a+1)+(1-p)*(2*b-a+2)

def back(case,n):
    if n==0: return keepgoing(case)
    p=right(case[1][:-n])
    [a,b]=case[0]
    return p*(b-a+1+2*n)+(1-p)*(2*b-a+2+2*n)

def best(case):
    b=[back(case,i) for i in range(case[0][0]+1)]
    return min(b+[giveup(case)])

def solve(cases):
    f=open('out.txt','w')
    for case in enumerate(cases,start=1):
        num,ans=case[0],best(case[1])
        f.write('Case #'+str(num)+': '+str(ans)+'\n')
    f.close()

if __name__=='__main__': solve(file2list(parse('A-small-attempt0.in')))
