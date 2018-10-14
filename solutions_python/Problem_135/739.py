def commonstart():
    fin=open(r'C:\Users\Administrator\Desktop\google jam\2014\Magic Trick\A-small-attempt0.in','r')
    fout=open(r'C:\Users\Administrator\Desktop\google jam\2014\Magic Trick\A.out','w')
    return fin,fout
fin,fout=commonstart()
num=int(fin.readline())
for line in range(0,num):
    mark=0
    result=list()
    first=int(fin.readline())
    arr1=list()
    for each in range(0,4):
        arr1.append(list(map(int,fin.readline().split())))
    second=int(fin.readline())
    arr2=list()
    for each in range(0,4):
        arr2.append(list(map(int,fin.readline().split())))
    print(arr1,arr2)
    for itt1 in arr1[first-1]:
        for itt2 in arr2[second-1]:
            print(itt1,itt2)
            if itt1==itt2:
                if itt1 not in result:
                    result.append(itt1)
    print(result)
    if len(result)==0:
        print('Case #%s: Volunteer cheated!'%(line+1),file=fout)
    elif len(result)==1:
        print('Case #%s: %s'%(line+1,result[0]),file=fout)
    else:
        print('Case #%s: Bad magician!'%(line+1),file=fout)
fin.close()
fout.close()
    
        
