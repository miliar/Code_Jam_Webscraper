
input=file('A-large.in','r')
output=file('output11.out','w')
def proc_case():
    length=int(input.readline())
    v1=map(int,input.readline().split())
    v2=map(int,input.readline().split())

    v1.sort()
    v2.sort()
    v2.reverse()    

    scalar=0    
    for i in range(length):
        scalar+=v1[i]*v2[i]

    return ' '+str(scalar)        

        
def proc_all():
    case_count=input.readline()

    for i in range(1,int(case_count)+1):
        output.write('Case #'+str(i)+':'+proc_case()+'\n')

proc_all()

input.close()
output.close()