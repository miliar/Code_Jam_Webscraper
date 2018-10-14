
# coding: utf-8

# Input
# 
# The first line of the input gives the number of test cases, T; T test cases follow. Each test case begins with two integers D and N: the destination position of all of the horses (in kilometers) and the number of other horses on the road. Then, N lines follow. The i-th of those lines has two integers Ki and Si: the initial position (in kilometers) and maximum speed (in kilometers per hour) of the i-th of the other horses on the road.
# 
# Output
# 
# For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the maximum constant speed (in kilometers per hour) that Annie can use without colliding with other horses. y will be considered correct if it is within an absolute or relative error of 10-6 of the correct answer. See the FAQ for an explanation of what that means, and what formats of real numbers we accept.

# In[19]:

def readInput(filename):
    f=open(filename, 'r')
    inputVals=f.read()
    f.close()
    inputList=[]
    string=''
    for i in xrange(len(inputVals)):
        if inputVals[i]=='\n':
            inputList.append(string)
            string=''
        else:
            string+=inputVals[i]

    if string !='': #otherwise extra new line at EOF can cause failure.
        inputList.append(string)
    #if len(inputList)!=int(inputList[0])+1:
    #    print "Error! Length mismatch."
    del inputList[0]
    return inputList


# In[11]:

def parseInput(line):
    #make sure you don't accidently assume things like
    #numbers are only one character long
    k,s=line.split()
    k=int(k)#very important!!! 8<'3'
    s=int(s)
    return (k,s)


# In[ ]:




# In[28]:

def main(inputList):
    f=open(outputFile, 'w')
    i=0
    case=0
    while i<len(inputList):
        D,N=inputList[i]
        ks=[]
        for j in range(i+1,i+N+1):
            ks.append(inputList[j])
        i+=N+1
        out=solveProblem((D,ks))
        string="Case #{0}: {1}\n".format(case+1, out)
        case+=1
        f.write(string)
    f.close()


# 

# 

# In[30]:

def solveProblem(inp):
    d,ks=inp
    time=0.0000001
    for k,s in ks:
        t=(d-k)*1.0/(s*1.0)
        time=t if t>time else time
    return d*1.0/time


# In[5]:

def bruteForce(inp):
    pass


# In[ ]:




# In[33]:

filename='A-small-attempt0'
outputFile=filename+'.out'
inputFile=filename+'.in'
inputList=[parseInput(line) for line in readInput(inputFile)]
main(inputList)


# In[ ]:




# In[ ]:



