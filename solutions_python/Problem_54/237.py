'''
Created on May 8, 2010

@author: AliJ
'''

def parse_num():
    return map(int, raw_input().split())

def gcd(a,b):
    if a==b:
        return a
    
    if a<b:
        (a,b)=(b,a)
        
    while a%b != 0:
        (a,b)=(b,a%b)
        
    return b


def process_case():
    theEvents=parse_num()[1:]
    N=len(theEvents)
    theEvents.sort()
    
    theDifferences=[]
    for i in range(1,N):
        if theEvents[i] != theEvents[i-1]:
            theDifferences.append(theEvents[i]-theEvents[i-1])
        
    g=theDifferences[0]
    
    for i in range(1,len(theDifferences)):
        g=gcd(theDifferences[i],g)
    
    return (-theEvents[0])%g
    

numCases = int(raw_input())



for i in range(numCases):
            
    print "Case #"+str(i+1)+":", (process_case())
