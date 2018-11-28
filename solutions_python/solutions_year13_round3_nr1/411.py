'''
Created on May 12, 2013

@author: akshay
'''

vowels = ["a","e","i","o","u"]

def findSubstrings(string):
    subStrings=[]
    j=1
    while True:
        for i in range(len(string)-j+1):
            subStrings.append(string[i:i+j])
        if j==len(string):
            break
        j+=1
        #string=string[1:]
    return subStrings

def findNvalue(subStr,n,vowels):
    N=0
    for i in subStr:
        if len(i)>=n:
            count=0
            for j in i:
                if j not in vowels:
                    count+=1
                if j in vowels and count<n:
                    count=0
            if count>=n:
                N+=1
    return N

fp = open("A-small-attempt0 (4).in","r")
list=fp.readlines()
list=[x.strip() for x in list]
list=[x.split() for x in list]
T=int(list.pop(0)[0])
for i in range(len(list)):
    list[i][1] = int(list[i][1])

for i in range(len(list)):
    string=list[i][0]
    n=list[i][1]
    print "Case #%d: %d"%(i+1,findNvalue(findSubstrings(string),n,vowels))

#print findSubstrings("quartz")
#print findNvalue(findSubstrings("quartz"),3,vowels)