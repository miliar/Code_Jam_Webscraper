'''
Created on May 22, 2010

@author: AliJ
'''


limit = 501
choose = [[0 for i in range(limit)] for i in range(limit)]

A = [[0 for i in range(limit)] for i in range(limit)]

pure = [0 for i in range(limit)]



def fillChoose():
    for i in range(limit):
        choose[i][0] = 1
        choose[i][i] = 1
    
    for i in range(limit):
        for j in range(1,i):
            choose[i][j] = choose[i-1][j-1] + choose[i-1][j]
            
            
def doChoose(i,j):
    if i >= j:
        return choose[i][j]
    else:
        return 0
    
def fillA():
    A[2][1] = 1
    for i in range(3, limit):
        A[i][1] =1
        A[i][2]= 1
        A[i][i-1] = 1
    
    for y in range(4, limit):
        for k in range(3, y-1):
            newVal = 0
            for i in range(1,k):
                newVal = (newVal+(doChoose(y-k-1,k-1-i)*A[k][i]))%100003
            A[y][k]= newVal
                

def fillPure():
    for i in range(2,limit):
        newVal = 0
        for k in range(1,i):
            newVal = (newVal+A[i][k])%100003
        pure[i]=newVal         

def parse_num():
    return map(int, raw_input().split())


def process_case():
    n = int(raw_input())
    return pure[n]

numCases = int(raw_input())
fillChoose()
fillA()
fillPure()





for i in range(numCases):
            
    print "Case #"+str(i+1)+":", (process_case())
    