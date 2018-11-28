f=open('A-small-attempt4.in')
lines = f.readlines()
answer=[]
number = 1
index1 = 1
index2 =6
n=1
f=open('A-small-attempt4.out','w')
while(index1 and index2<len(lines)):
    a1=lines[index1]
    array1=(lines[int(a1)+index1].split(' '))
    index1=index1+10
    a2=lines[index2]
    array2=(lines[int(a2)+index2].split(' '))
    index2=index2+10

    for x in array1:
        for y in array2:
            if int(x)==int(y):
                answer.append(x)
                
    if len(answer)==1:
        print('Case #'+str(n)+": "+str(answer[0]))
        f.write('Case #'+str(n)+": "+str(answer[0]+'\n'))
    if len(answer)==0:
        print('Case #'+str(n)+": "+'Volunteer cheated!')
        f.write('Case #'+str(n)+": "+'Volunteer cheated!'+'\n')
    if len(answer)>1:
        print('Case #'+str(n)+": "+'Bad magician!')
        f.write('Case #'+str(n)+": "+'Bad magician!'+'\n')
        
    answer=[]
    n=n+1
    
f.close()
f.close()
                    
