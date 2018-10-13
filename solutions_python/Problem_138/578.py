def calc():
    n=int(fin.readline())
    data1=list(map(float,fin.readline().split(' ')))
    data1.sort()
    data2=list(map(float,fin.readline().split(' ')))
    data2.sort()
    return str(calc2(n,data2,data1))+' '+str(n-calc2(n,data1,data2))

def calc2(n,data1,data2):
    ans=0
    j=0
    for i in range(0,n):
        while j<n and data1[i]>data2[j]:
            j+=1
        if j<n:
            ans+=1
            j+=1
    return ans

if __name__=='__main__':
    fin=open('input.txt','r')
    fout=open('output.txt','w')
    cases=int(fin.readline())
    for i in range(1,cases+1):
        fout.write('Case #{}: {}\n'.format(i,calc()))
    fin.close()
    fout.close()
