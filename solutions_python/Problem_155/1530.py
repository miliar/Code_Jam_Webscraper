def str2list(n):
    return [int(e) for e in n]

def howmany(li,m):
    ans=0
    up=0
    shynum=0
    while shynum<=m:
        if shynum<=up:
            up+=li[shynum]
            shynum+=1
        else:
            ans+=1
            up+=1
    return ans

        
def parseline(line):
    [m,st]=line.split()
    return howmany(str2list(st),int(m))


if __name__=='__main__':
    cases=int((input().split())[0])
    for i in range(cases):
        line=input()
        print("Case #"+str(i+1)+": "+str(parseline(line)))
