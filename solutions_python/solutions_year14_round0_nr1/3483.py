f=open('A-small-attempt0.in','r')

x=int(f.readline()[:-1])

for i in range(x):
    answer=[]
    a=int(f.readline()[:-1])
    a1=f.readline()[:-1].split()
    a2=f.readline()[:-1].split()
    a3=f.readline()[:-1].split()
    a4=f.readline()[:-1].split()
    arrange1=[a1,a2,a3,a4]
    b=int(f.readline()[:-1])
    b1=f.readline()[:-1].split()
    b2=f.readline()[:-1].split()
    b3=f.readline()[:-1].split()
    b4=f.readline()[:-1].split()
    arrange2=[b1,b2,b3,b4]

    for number in arrange1[a-1]:
        if number in arrange2[b-1]:
            answer.append(int(number))

    if len(answer)==1:
        print('Case #' + str(i+1) + ': ' + str(answer[0]))
    elif len(answer)>1:
        print('Case #' + str(i+1) + ': Bad magician!')
    else:
        print('Case #' + str(i+1) + ': Volunteer cheated!')
        
