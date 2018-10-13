fin=open('tidy.in','r')
fout=open('tidy.out','w')
tc=int(fin.readline())
for c in range(tc):
    n=int(fin.readline())
    i=n
    while i>0:
        sv=str(i)
        pos=0
        inc=True
        for ch in sv:
            if pos>0 and ch<sv [pos-1]:
                inc=False
                break
            pos+=1
        if inc:
            fout.write('Case #'+str(c+1)+': '+str(i)+'\n')
            break
        i-=1
fin.close()
fout.close()
