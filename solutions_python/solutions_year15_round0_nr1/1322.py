def go():
    f=open('1.in')
    c=int(f.readline())
    for case in range(1,c+1):        
        print 'Case #%d:'%case,
        print solve(f.readline())
    f.close()

    

def solve(s):
    l=[int(x) for x in s.split()[1]]
    need=0
    count=l[0]
    for x in range(1,len(l)):
        if count<x:
            dif=x-count
            need+=dif
            count+=dif
        count+=l[x]
    return need
        
