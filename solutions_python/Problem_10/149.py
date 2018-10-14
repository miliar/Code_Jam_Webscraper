

input=file('A-large.in','r')
output=file('output.txt','w')
def proc_case():
    P,K,L=map(int,input.readline().split())
    LList=map(int,input.readline().split())

    LList.sort()

    count=0

    for i in range(1,P+1):
        for j in range(K):
            if len(LList)==0:break
            count+=LList.pop()*i
    if len(LList)!=0:
        return ' IMPOSSIBLE'
    return ' '+str(count)


        
def proc_all():
    case_count=input.readline()

    for i in range(1,int(case_count)+1):
        output.write('Case #'+str(i)+':'+proc_case()+'\n')

proc_all()
input.close()
output.close()