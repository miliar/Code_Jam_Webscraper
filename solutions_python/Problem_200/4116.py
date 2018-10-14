import sys

def remove_zero(n):
    while n[0]=='0':
        n=n[1:]
    return n

def gettidy(arr,i):
    arr[i+1:] = [9] * (len(arr)-i-1)
    t=''.join(str(x) for x in arr)
    return t

def checkprevious(arr,i):
    if i==0:
        return True
    if arr[i-1]<arr[i]:
        return True
    return False

def goback(arr,i):
    while i>0:
        if arr[i-1]==arr[i]:
            i=i-1
        else:
            return i
    if i==0:
        return 0

def istidy(n):
    if n<9:
        return n
    l=0
    arr=[]
    or_n=n
    #get index of the first smaller number
    while n>9:
        l+=1
        t=n%10
        n=n/10
        arr.append(t)
    arr.append(n)
    arr=arr[::-1]
    i=0
    while i<len(arr)-1:
        if arr[i]>arr[i+1]:
            if checkprevious(arr,i):
                arr[i]=arr[i]-1
                return gettidy(arr,i)
            else:
                j = goback(arr,i)
                arr[j]=arr[j]-1
                return gettidy(arr,j)
        i=i+1
    return or_n

with open(sys.argv[1]) as f:
    lines=f.readlines()

lines=[x.strip() for x in lines]
lines = map(int,lines)
t=int(lines[0])
for i in range(1,t+1):
    n=lines[i]
    t= int(istidy(n))
    print "Case #{0:1}: {1}".format(i,t)
