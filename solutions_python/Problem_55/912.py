#Dummy class
class Data():
    pass

#Returns a class data with t, input [r/k/n/G] attributes)
def readin(f):
    a = f.readline
    data=[]
    string = a().split()
    data=Data()
    #No of inputs T
    data.t=long(string[0])
    data.input=[]
    for i in range(data.t):
        string = a().split()
        data.input.append([])
        #No of rounds R
        data.input[i].append(long(string[0]))
        #No of Seats K
        data.input[i].append(long(string[1]))
        #No of groups N
        data.input[i].append(long(string[2]))
        string = a().split()
        G=[]
        for j in range (long(data.input[i][2])):
            G.append(long(string[j]))
        data.input[i].append(G)
    return data

#Function returns the money in a perticular situation
def money(r,k,n,g):
    g_now=[]
    m=long(0)
    persons=0
    for i in range(n):
        g_now.append(g[i])
    for i in range(n):
        persons+=g[i]
    #print g_now
    #print persons
    for i in range(r):
        s=0
        j=0
    
        if persons <= k :
            m=persons*r
        else:
            while (s <= k):
                s_old=s
                s+=g_now[j]
                j+=1
            s=s_old
            j-=1
            g_now=g_now[j:]+g_now[:j]
            #print g_now
        m+=s
    return long(m)


f=open('C-small-attempt0.in')
data = readin(f)
f.close()
f=open('C-small-attempt0.out','w')
for i in range(data.t):
    input=data.input[i]
    m=money(input[0],input[1],input[2],input[3])
    string = 'Case #%d: %d' %(i+1,m)
    print string
    f.write(string+'\n')
f.close()
