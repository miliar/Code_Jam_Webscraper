'''arr=[]
for i in range(10):
    arr.append(0)'''

def isTidy(t):
    s=str(t)
    i=0
    while i<len(s):
        a=s[i]
        for j in s[i:]:
            if a>j:
                return False
        i+=1
    return True

def makeTidy(t):
    s=str(t)
    i=0
    while i<len(s):
        a=s[i]
        for j in s[i:]:
            if a>j:
                index=s.find(j,i+1)
                arr=[]
                for k in s:
                    arr.append(k)
                k=index
                while k<len(arr):
                    arr[k]='9'
                    k+=1
                d=int(s[index-1])-1
                arr[index-1]=str(d)
                st=''
                for b in arr:
                    st=st+b
                return makeTidy(int(st))
        i+=1
    return s

arr=[]
f=open('Input.txt','r')
for word in f:
    arr.append(int(word))

del arr[0]
i=1
for inp in arr:
    s='Case #'
    b=': '
    if isTidy(inp):
        print(s+str(i)+b+str(inp))
        i+=1
        continue
    print(s+str(i)+b+str(makeTidy(inp)))
    i+=1
