#!/usr/bin/python


inName = "B-small-attempt3.in"
outName = "B-small-attempt3.out"

inFile = open(inName, 'r')
inData = inFile.readlines()
inFile.close()

#print inData

outFile = open(outName, 'wt')

numTest = int(inData[0].replace('\n',''))
r = 1

def check_col(j, data):
    #print data
    num_begin = data[0][j]
    for i in range(len(data)):
        if(num_begin != data[i][j]):
            return 0
    return 1
    

def isPossible(data):
    for i in range(len(data)):
        num = 1
        for j in range(len(data[i])):
            if (2 == int(data[i][j])):
                num = 2
        if ( 2 == num ):
            for j in range(len(data[i])):
                if (1 == int(data[i][j])):
                    #print str(num_begin)+ str(data[i][j]) +" is different"
                    if(0==check_col(j, data)):
                        return 0
    return 1
            

for num in range(numTest):
    data = []
    width = inData[r].replace('\n','').split(' ')
    r += 1
    for _ in range(int(width[0])):
        data.append(inData[r].replace('\n','').split(' '))
        r += 1
    print isPossible(data)
    outFile.write("Case #"+str(num+1)+": ")
    
    if (1==isPossible(data)):
        outFile.write("YES")
    else:
        outFile.write("NO")

    outFile.write("\n")








