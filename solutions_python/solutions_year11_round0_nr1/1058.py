def findNextMove(color,completed):
    next=0
    for x in range(completed, numButtons):
        if colors[x]==color:
            next=numbers[x]
            break
    return next

inputFile=open('cja_input_lg.txt','r')
outputFile=open('cja_output.txt','w')
numCases=int(inputFile.readline())

for line in range(numCases):
    input=inputFile.readline().strip('\n')
    input=input.split(' ')
    numButtons=int(input[0])
    input=input[1:]
    colors=[]
    numbers=[]
    s="OB"
    for x in range(numButtons):
        colors+=[s.find(input[2*x])]
        numbers+=[int(input[2*x+1])]

    time=0
    comp=0
    pos=[1,1]
    nextMove=[findNextMove(0,0),findNextMove(1,0)]
    while comp!=numButtons:
        time+=1
        a=colors[comp]
        b=abs(a-1)
        if pos[b]<nextMove[b]:
            pos[b]+=1
        elif pos[b]>nextMove[b]:
            pos[b]-=1
        if pos[a]==nextMove[a]:
            comp+=1
            nextMove[a]=findNextMove(a,comp)
        elif pos[a]<nextMove[a]:
            pos[a]+=1
        elif pos[a]>nextMove[a]:
            pos[a]-=1
            
    outputFile.write('Case #'+str(line+1)+": "+str(time)+'\n')

outputFile.close()
inputFile.close()
