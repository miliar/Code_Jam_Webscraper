
def Need(x,y):
    global i
    global xtra
    global people
    if people>i:
        people+=y
    else:
        xtra+=i-people+1
        people+=y+i+1-people
t=int(input())
Xtra=[]
for w in range(t):
    In=input()
    In=In.split()
    i=0
    xtra=0
    people=int(In[1][0])
    for j in range(len(In[1])-1):
        Need(int(In[1][j]),int(In[1][j+1]))
        i+=1
    Xtra.append(xtra)
    ##print('Case','#'+str(w+1)+':',xtra)
b=1
for e in Xtra:
    print('Case','#'+str(b)+':',e)
    b+=1

































