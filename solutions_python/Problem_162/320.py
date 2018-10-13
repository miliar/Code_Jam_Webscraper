def read_input_1():
    fin=open('input1.txt','r')
    flines=fin.readlines()
    fin.close()
    Ns=[]
    for i in range(1,len(flines)):
        Ns.append(int(flines[i]))
    return Ns

def solve1(PC):
    Ns=read_input_1()
    fout=open('output1.txt','w')
    for i in range(len(Ns)):
        fout.write('Case #'+str(i+1)+': '+str(PC[Ns[i]])+'\n')
    fout.close()

def precompute(N):
    data={}
    for i in range(1,13):
        data[i]=i
    for i in range(13,N):
        a=data[i-1]+1
        temp=int(str(i)[::-1])
        if int(str(temp)[::-1])==i:
            try:
                b=data[temp]+1
            except KeyError:
                b=N+1
        data[i]=min((a,b))
    return data
    
          