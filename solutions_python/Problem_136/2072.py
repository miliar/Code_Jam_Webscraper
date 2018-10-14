#__author__ = 'afonso-ferreira'
file = open('B-large.in', 'r')
matrix=file.read().split('\n')
for aux in range(1,int(matrix[0])+1):
    numbers=matrix[aux].split(' ')
    numbers=[float(i) for i in numbers]
    n=-1
    dif=-1
    while(dif<0):
        n=n+1
        dif=numbers[2]/(2+(n+1)*numbers[1]) +numbers[0]/(2+n*numbers[1])-numbers[2]/(2+n*numbers[1])
    time=numbers[2]/(2+n*numbers[1])
    for aux2 in range(n-1,-1,-1):
        time=time+numbers[0]/(2+aux2*numbers[1])
    print('Case #',end="")
    print(aux,end="")
    print(":",end=" ")
    print("%.7f" % time)