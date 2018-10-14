import psyco
psyco.full()
def makedir(r,s):
    ct=0
    dir=s.split("/")[1:]
    #print dir
    cur=r
    for sd in dir:
        if sd not in cur:
            cur[sd]={}
            ct+=1
        cur=cur[sd]
    return ct
fin=file("a.in")
fout=file("a.out","w")
T=int(fin.readline().strip())
for t in range(T):
    N,M=[int(_) for _ in fin.readline().strip().split()]
    root={}
    for n in range(N):
        d=fin.readline().strip()
        makedir(root,d)
    ct=0
    for m in range(M):
        d=fin.readline().strip()
        ct+=makedir(root,d)
    rst="Case #%d: %d\n"%(t+1,ct)
    print rst,
    fout.write(rst)
fout.close()
    