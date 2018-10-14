fin=open('c:\\contest\\tst1.txt', 'r')
fout=open('c:\\contest\\outputfile.txt','w')
l=fin.readlines()
N=int(l[0])
ser='welcome to code jam'
serl=len(ser)
for i in range(1,N+1):
    cur=l[i]
    curlist=[[0 for j in xrange(0,serl)] for let in cur]
    curlen=len(cur)
    for j in xrange(curlen-1,-1,-1):
        curlist[j][serl-1]+=(cur[j]=='m')
        #print (repr(j)+','+repr(17)+','+repr(curlist[j][15]))
        for k in xrange(serl-2,-1,-1):
            if cur[j]==ser[k]:
                curlist[j][k]+=sum([curlist[g][k+1] for g in xrange(curlen-1,j,-1)])
            #print (repr(j)+','+repr(k)+','+repr(curlist[j][15]))
    tot=sum([curlist[g][0] for g in xrange(0,curlen)])
    #for k in xrange(0,curlen):
    #    print repr(i)+','+repr(k)+','+repr(curlist[g][0])
    fout.write('Case #'+repr(i)+': '+str(tot).zfill(4)[-4:]+'\n')
fin.close()
fout.close()
