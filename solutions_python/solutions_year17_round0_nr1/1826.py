import random
t=int(input())
f=open('/home/shubham/python_scripts/outputQ1Long.txt',"w")
flip=['-','+']


for q in range(t):
    s,k=input().split(' ')
    s=list(s)
    k=int(k)
    count=0
    for i in range(len(s)-k+1):
        if(s.__contains__('-') and s[i]=='-'):
            sub=s[i:i+k]
            #print("substring =",sub)
            for j in range(len(sub)):
                s[i+j]=flip[1-flip.index(sub[j])]
            count+=1
            #print("substring after change= ",str(s))
    if(s.__contains__('-')):
        f.write("Case #%d: IMPOSSIBLE\n"%(q+1))
    else:
        f.write("Case #%d: %d\n"%(q+1,count))
        #print(s)

"""q=0
def check(s,k):
    global flip
    global f
    global q
"""


"""x=[]
for i in range(1000):
    y=[]
    for j in range(random.randint(900,1000)):
        y.append(flip[random.randint(0,1)])
    x.append(y)
for i in x:
    print(''.join(i))
for i in x:
    check(i,random.randint(1,12))
"""