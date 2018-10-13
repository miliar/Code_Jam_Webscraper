import math
import time
global a
a=open("C-large-1.in","r")
global arr
arr=[]
def GetPolindromes():
    global arr
    i=1
    while(i<=10**7):
        if(IsPolindrome(i)==True):
            if(IsPolindrome(i*i)==True):
                arr+=[i*i]
        i+=1
    return arr
def IsPolindrome(num):   
    s=str(num)
    i=0   
    while(i<len(s)/2):        
        if(s[i]!=s[len(s)-i-1]):
            return False
        i+=1        
    return True

line=a.readline()
T=int(line[:len(line)-1])
#T=int(input(""))
i=1
AB=[]
while(i<=T):
    line=a.readline()
    AB+=[line[:len(line)-1]]
    #AB+=[str(input(""))]
    i+=1
i=0
GetPolindromes()
while(i<T):    
    j=0
    firstnum=""
    lastnum=""
    isAfterSpace=False
    while(j<len(AB[i])):
        if(AB[i][j]!=" "):
            if(isAfterSpace==False):
                firstnum+=AB[i][j]
            else:
                lastnum+=AB[i][j]
        else:
            isAfterSpace=True
        j+=1
    f=eval(firstnum)
    l=eval(lastnum)    
    count=0
    k=0    
    while(k<len(arr)):
        if(arr[k]>=f and arr[k]<=l):
            count+=1        
        k+=1    
    print("Case #"+str(i+1)+": "+str(count))
    i+=1   
