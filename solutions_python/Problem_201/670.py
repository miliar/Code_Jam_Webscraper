def findStall(n,k):
    i=0
    base_sum=0
    while base_sum+2**i<k:
        base_sum+=2**i
        i+=1
    if k-base_sum>(n-base_sum)%2**i:
        target_space=(n-base_sum)/2**i
    else:
        target_space=(n-base_sum)/2**i+1
    if target_space==1:
        return 0,0
    elif target_space%2==0:
        r=target_space/2
        return r,r-1
    else:
        r=target_space/2
        return r,r
        
def main(fin,fout):
    numCases=int(fin.readline())
    for i in range(numCases):
        case=fin.readline()
        case=case.split()
        n=int(case[0])
        k=int(case[1])
        l,r=findStall(n,k)
        fout.write('Case #'+str(i+1)+': '+str(l)+' '+str(r)+'\n')

fin=open('C:\\Users\\Andri_000\\Downloads\\3.in','r')
fout=open('C:\\Users\\Andri_000\\Downloads\\3.out','w')
main(fin,fout)
fin.close()
fout.close()