import string
name='B-large'
fileinput=open(name+'.in' ,'r')
input=fileinput.read().splitlines()
fileinput.close()
fileoutput=open(name+'.out' ,'w')
i=0
cases=int(input[i])
for case in range(0,cases):
    i+=1
    T = int(input[i])
    i+=1
    NA,demandA,sourceA = int(input[i].split(' ')[0]),[],[]
    NB,demandB,sourceB = int(input[i].split(' ')[1]),[],[]
    for j in range(0, NA):
        i+=1
        temp = input[i].split(' ')[0]
        demandA.append(60*int(temp.split(":")[0])+int(temp.split(":")[1]))
        temp = input[i].split(' ')[1]
        sourceB.append(60*int(temp.split(":")[0])+int(temp.split(":")[1])+T)
    for j in range(0, NB):
        i+=1
        temp = input[i].split(' ')[0]
        demandB.append(60*int(temp.split(":")[0])+int(temp.split(":")[1]))
        temp = input[i].split(' ')[1]
        sourceA.append(60*int(temp.split(":")[0])+int(temp.split(":")[1])+T)
    demandA.sort(reverse=True)
    demandB.sort(reverse=True)
    sourceA.sort(reverse=True)
    sourceB.sort(reverse=True)
    debugoutput=demandA,demandB,sourceA,sourceB
    j=0
    while j < sourceA.__len__() and demandA.__len__()>0:
        if sourceA[j] <= demandA[0]:
            del sourceA[j]
            del demandA[0]
        else:
            j+=1
    j=0
    while j < sourceB.__len__() and demandB.__len__()>0:
        if sourceB[j] <= demandB[0]:
            del sourceB[j]
            del demandB[0]
        else:
            j+=1
    print 'case' + str(case+1) + ' demand for A is ' + str(demandA.__len__()) + ' demand for B is ' + str(demandB.__len__())
    fileoutput.write('Case #' + str(case+1) + ': ' + str(demandA.__len__()) + ' ' + str(demandB.__len__()) + '\n')
fileoutput.close()
