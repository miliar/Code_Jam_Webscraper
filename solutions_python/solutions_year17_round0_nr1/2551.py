
# coding: utf-8

# In[2]:

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
    if len(inputList)!=int(inputList[0])+1:
        print "Error! Length mismatch."
    del inputList[0]
    return inputList


# In[3]:

def parseInput(line):
    #make sure you don't accidently assume things like
    #numbers are only one character long
    stack,k=line.split()
    k=int(k)#very important!!! 8<'3'
    stack=[(1 if d=='+' else 0) for d in stack]
    return (k,stack)


# In[4]:

test1=parseInput('---+-++- 3')
test2=parseInput('+++++ 4')
test3=parseInput('-+-+- 4')
print test1
print test2
print test3


# In[5]:

def main(inputList):
    f=open(outputFile, 'w')
    for i,inp in enumerate(inputList):
        out=solveProblem(inp)
        string="Case #{0}: {1}\n".format(i+1, out)
        f.write(string)
    f.close()


# "Given the current state of the pancakes, calculate the minimum number of uses of the oversized pancake flipper needed to leave all pancakes happy side up, or state that there is no way to do it."
# 
# Flipping doesn't change order or anything. Therefore all that matters is that all 1's (+'s) are flipped an even number of times and all 0's are flipped an odd number of times.
# 
# This is a possible DP problem. The solution for any subregion is independent of the rest, so the problem is instead to divide into optimal (minimizing necessary flips) subregions of length <2k.

# However, a simple greedy recursive solution solves this problem. Observe that each end pancake can only be flipped one possible way (by flipping the k-1 to the side of it). Therefore we flip each end 0 or 1 times, more flips are redundant and wasteful since order of flips is irrelevant. Now, cut off each end and repeat recursively.

# In[6]:

def solveProblem(inp):
    k,stack=inp
    flipcount=0
    if len(stack)==1 and k==1:
        return 1-stack[0]
    while True:
        if len(stack)<k:
            for cake in stack:
                if cake==0:
                    return 'IMPOSSIBLE'
            return flipcount
        elif len(stack)==k:
            if stack[0]!=stack[-1]:
                return 'IMPOSSIBLE'
            if stack[0]==0:
                flipcount+=1
                for k2 in xrange(k):
                    stack[k2]=1-stack[k2]
        else:
            if stack[0]==0:
                flipcount+=1
                for k2 in xrange(k):
                    stack[k2]=1-stack[k2]
            if stack[-1]==0:
                flipcount+=1
                for k2 in xrange(1,k+1):
                    stack[-k2]=1-stack[-k2]
        del stack[0]
        del stack[-1]


# In[7]:

print test1, solveProblem(test1)
print test2, solveProblem(test2)
print test3, solveProblem(test3)


# In[8]:

filename='A-large'
outputFile=filename+'.out'
inputFile=filename+'.in'
inputList=[parseInput(line) for line in readInput(inputFile)]
main(inputList)


# In[ ]:



