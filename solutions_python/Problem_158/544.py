def solve():
    x=d[0]
    rc=sorted(d[1::],reverse=True)
    if x ==1:
        return "GABRIEL"
    if x==2 and rc in [[2,1],[4,1],[2,2],[3,2],[4,2],[4,3],[4,4]]:
        return "GABRIEL"
    if x==3 and rc in [[3,2],[3,3],[4,3]]:
        return "GABRIEL"
    if x==4 and rc in [[4,3],[4,4]]:
        return "GABRIEL"
    return "RICHARD"

fin=open('../in','r') ; fout=open('../out','w')
cases=int(fin.readline().strip())
for case in range(1,cases+1):
    print case
    d=[int(x) for x in fin.readline().strip().split(' ')]
    fout.write("Case #"+str(case)+": "+str(solve()+"\n"))