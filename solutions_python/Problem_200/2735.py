
# coding: utf-8

# In[1]:

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


# In[2]:

def parseInput(line):
    return int(line)


# In[3]:

test1=parseInput('4')
test2=parseInput('132')
test3=parseInput('1000')
print test1
print test2
print test3


# In[4]:

def main(inputList):
    f=open(outputFile, 'w')
    for i,inp in enumerate(inputList):
        out=solveProblem(inp)
        string="Case #{0}: {1}\n".format(i+1, out)
        f.write(string)
    f.close()


# some integers, when written in base 10 with no leading zeroes, have their digits sorted in non-decreasing order. Some examples of this are 8, 123, 555, and 224488. She decided to call these numbers tidy. Numbers that do not have this property, like 20, 321, 495 and 999990, are not tidy.
# 
# She just finished counting all positive integers in ascending order from 1 to N. What was the last tidy number she counted?
# 
# 
# 

# Repeating the same digit over and over is always tidy. Therefore if we bruteforce, worst case is N=99...98 then 89...99~N*(9/10).
# 
# If not all 9s and leftmost 9->89..99
# If leftmost 8->89....9 or 889...9 or 8889...9 to 88...8
# for x<8, 8x...->79...9
# 
# Simply start at leftmost digit, go to next digit as long as non-decreasing. If it decreases, failing_digit-=1. Everything to the right=9s.

# In[5]:

def solveProblem(inp):
    digits=str(inp)
    max=0
    for i,char in enumerate(digits):
        dig=int(char)
        if dig>max:
            max=dig
        elif dig<max:
            #digits[i]<digits[i-1]
            break
    else:
        #the number itself was tidy.
        return inp
    j=1
    while i-1-j>=0 and digits[i-1]==digits[i-1-j]:
        j+=1
    adjusted_digits=int(digits[i-j:i])-int('1'*len(digits[i-j:i]))
    return int( digits[:i-j]+str(int(digits[i-j])-1)+'9'*len(digits[i-j+1:]) )
        
        


# In[6]:

def bruteForce(inp):
    def isTidy(integer):
        n=str(integer)
        max=0
        for char in n:
            if int(char)<max:
                return False
            elif int(char)>max:
                max=int(char)
        return True
    for n in xrange(inp,0,-1):
        if isTidy(n):
            return n


# In[7]:

print test1, solveProblem(test1), bruteForce(test1)
print test2, solveProblem(test2), bruteForce(test2)
print test3, solveProblem(test3), bruteForce(test3)


# In[10]:

filename='B-small-attempt1'
outputFile=filename+'.out'
inputFile=filename+'.in'
inputList=[parseInput(line) for line in readInput(inputFile)]
main(inputList)


# In[11]:

import random
order=range(len(inputList))
random.shuffle(order)
j=0
while True:
    try:
        i=order.pop()
        assert(solveProblem(inputList[i])==bruteForce(inputList[i]))
    except AssertionError:
        print 'Error #',j
        print 'Case',i,':',inputList[i]
        print solveProblem(inputList[i])
        print bruteForce(inputList[i])
        j+=1
        if j>3:
            break
    except IndexError:
        print 'success'
        break


# In[ ]:



