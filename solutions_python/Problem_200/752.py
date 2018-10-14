rnd="p17Q"
pb="B"
size="Large"
fin=open("C:\F\workspace\Euler\EulerProject\GCJam\%s\%s-%s.in"%(rnd,pb,size),'r')
fout=open("C:\F\workspace\Euler\EulerProject\GCJam\%s\%s-%s.out"%(rnd,pb,size),'w')

T=int(fin.readline())
print T
for i in range(1,T+1):
    sN=fin.readline().strip()

    res=""
    last_dig="0"
    ix=0
    ix_tokeep=0
    prev_dig="0"
    while ix<len(sN) and sN[ix]>=last_dig:
        if sN[ix]>last_dig:#higher than previous so the left is good to keep
            ix_tokeep=ix 
            #prev_dig=last_dig
            last_dig=sN[ix]
        print ix,sN[ix],last_dig,ix_tokeep
        ix+=1
    if ix<len(sN):#not tidy
        print ix,len(sN),"not tidy"
        res=str(int(sN[:ix_tokeep]+str(int(sN[ix_tokeep])-1)+"9"*(len(sN)-ix_tokeep-1)))
    else:#tidy so no change
        print ix,len(sN),"tidy"
        res=sN
            
    x=0
    line="Case #%d: %s" % (i, res)#
    print line
    fout.write(line+"\n")
fout.close()