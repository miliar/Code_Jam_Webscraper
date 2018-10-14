inputFile=file('input.txt','r')

firstLine=inputFile.readline()
n=int(firstLine)
outputString=''
line=inputFile.readline()

for i in range(n):
    firstAnswer=int(line)
    for k in range(firstAnswer):
        line=inputFile.readline()
    L1=[int(integer) for integer in line.split(' ')]

    for k in range(5-firstAnswer):
        line=inputFile.readline()

    secondAnswer=int(line)

    for k in range(secondAnswer):
        line=inputFile.readline()
    L2=[int(integer) for integer in line.split(' ')]

    for k in range(5-secondAnswer):
        line=inputFile.readline()

    c=set(L1)&set(L2)
    size=len(c)

    if size==0:
        outputString+="Case #"+str(i+1)+": Volunteer cheated!\n"
    elif size==1:
        outputString+="Case #"+str(i+1)+": "+str(c.pop())+"\n"
    else:
        outputString+="Case #"+str(i+1)+": Bad magician!\n"

outputFile=open('output_problem_a.txt','w')
outputFile.write(outputString)
outputFile.close()
inputFile.close()
