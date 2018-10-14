import sys
import copy
dictionary=[]
sys.stdin = open('A-small-attempt2.in','r')
l,d,n = [int(i) for i in input().split()]
def fun(tokens):
    global dictionary,l,d
    k=['']
    for i in range(l):
        lis=[]
        for j in tokens[i]:
            for m in k:
                for item in dictionary:
                    if(item.startswith(m+j)):
                        lis.append(m+j)
                        break
                    
        k=lis
    print('A')
    print(lis)
    print('B')
    return len(lis)
        
canOccuratPosition=[]
tokens=[]
for i in range(l):
    b=[]
    c=''
    for j in range(26):
        b.append(0)
    canOccuratPosition.append(b)
    tokens.append(c)
output=open('output.txt',mode='w')
for i in range(d):
    dictionary.append(input())
    for j in range(len(dictionary[i])):
        canOccuratPosition[j][ord(dictionary[i][j])-ord('a')]=1
dictionary.sort()
print(dictionary)
for i in range(n):
    k=0
    resetTokens=copy.deepcopy(tokens)
    mf=0
    a=input()
    j=0
    while(j<len(a)):
        if(a[j]=='('):
            j+=1
            while(a[j]!=')'):
                if(canOccuratPosition[k][ord(a[j])-ord('a')]):
                    if(a[j] not in tokens[k]):
                        tokens[k]+= a[j]
                j+=1
            if(a[j]==')'):
                j+=1
        else:
            if(canOccuratPosition[k][ord(a[j])-ord('a')]):
                if(a[j] not in tokens[k]):
                    tokens[k]+= a[j]
            j+=1
        if(tokens[k] is ''):
            mf=1
        k+=1  
    if(mf==1):
        print('Case #',i+1,': 0',file=output,sep='')
    else:
        for j in tokens:
            ''.join(sorted(iter(j)))
        print('Case #',i+1,': ',fun(tokens),file=output,sep='')
    tokens=copy.deepcopy(resetTokens)

