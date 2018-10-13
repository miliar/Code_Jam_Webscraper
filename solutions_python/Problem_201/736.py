rnd="p17Q"
pb="C"
size="large"
fin=open("C:\F\workspace\Euler\EulerProject\GCJam\%s\%s-%s.in"%(rnd,pb,size),'r')
fout=open("C:\F\workspace\Euler\EulerProject\GCJam\%s\%s-%s.out"%(rnd,pb,size),'w')

T=int(fin.readline())
print T
for i in range(1,T+1):
    sN,sK=fin.readline().strip().split()
    N,K=int(sN),int(sK)
    print N,K
    dic={N:1}#1 range of N stalls
    k=K
    while k>0:
        biggest_range_size=max(dic)
        biggest_range_qty=dic[biggest_range_size]
        MIN=(biggest_range_size-1)/2
        MAX=biggest_range_size-1-MIN
        for half_size in (MAX,MIN):
            if half_size in dic:
                dic[half_size]+=biggest_range_qty
            else:
                dic.update({half_size:biggest_range_qty})
        del dic[biggest_range_size]
        k-=biggest_range_qty

    res="%d %d" % (MAX,MIN)
    line="Case #%d: %s" % (i, res)#
    print line
    fout.write(line+"\n")
fout.close()