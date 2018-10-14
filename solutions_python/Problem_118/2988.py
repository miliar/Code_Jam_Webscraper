import math
# Procedure To Check If Entered Number Is A Palindrome
def pal(n):
    n=str(n)
    arr=[]
    for i in range(len(n)):
        arr.append(n[i])

    arrev=[]
    for i in reversed(arr):
        arrev.append(i)
    for i in range(len(arr)):
        if arr[i]!=arrev[i]:
            return 0
    return 1
    
def fairsquare(n):
    if pal(n)!=1:
        return 0        #The Number Is Not A Palindrome
    root=math.sqrt(int(n))
    if root-int(root)!=0:
        return 0
    if pal(int(math.sqrt(int(n))))!=1:
        return 0        #The Root Of The Number Is Not Palindrome
    return 1

# The Actual Program Starts Here
filename = open('C-small-attempt0.in','r')
no=int(filename.readline()) #Number Of Test Cases
countarray=[]       #Counter Array
for i in range(no):
    a=filename.readline()
    a=a.split(' ')
    b = int(a[1])
    a = int(a[0])
    # Check Every Number To Be FairSquare Within Given Range
    count=0
    for i in range(a,b+1):
        if fairsquare(i)==1:
            count+=1
    countarray.append(count)
filename.close()
filename = open('Output.txt','w')

for i in range(len(countarray)):
    filename.write('Case #'+str(i+1)+': '+str(countarray[i])+'\n')

filename.close()  

