def magic(il,com,de):
    sl=[]
    sl.append(il[0])
    lastsl=sl[0]
    for i in range(1,len(il)):
        temp=il[i]
        if(com.has_key((lastsl,temp))):
            sl[-1]=com[lastsl,temp]
        elif(find_op(list(sl),temp,de)):
            sl=[]
            lastsl=None
        else:
            sl.extend(temp)
        if(len(sl)!=0):
            lastsl=sl[-1]
    return sl
def find_op(ls,t,d):
    found=False
    ls.append(t)
    for e in d:
        if e.issubset(ls):
            found=True
            break
    return found
def write(sol_list):
    f=open('a.out','w')
    i=0
    for element in sol_list:
        i+=1
        string_a=""
        for letter in element:
            string_a+=letter+', '
        s="Case #{}: [{}]\n".format(i,string_a.strip(', '))
        f.write(s)
    f.close()

def run():
    f=open('B-small-attempt0.in','r')
    T=int(f.readline().strip('\n'))
    a=[]
    for i in range(T):
        print i
        temp=f.readline().strip('\n').split(' ')
        C=int(temp.pop(0))
        combinations=dict()
        deletions=[]
        for i in range(C):
            t=temp.pop(0)
            combinations[(t[0],t[1])]=t[2]
            combinations[(t[1],t[0])]=t[2]
        D=int(temp.pop(0))
        for i in range(D):
            t=temp.pop(0)
            o=set((t[0],t[1]))
            deletions.append(o)
        N=int(temp.pop(0))
        cstring=temp.pop()
        if(len(cstring)!=N):
            print "read error"
        w=magic(cstring,combinations,deletions)
        a.append(w)
    f.close()
    return a
sol=run()
write(sol)
#print a
