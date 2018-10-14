import numpy as np

def read_data2():
    fin=open('B-small-attempt4.in','r')
    flines=fin.readlines()
    data=[]
    for i in range(2,len(flines),2):
        temp=flines[i].split()
        d=[]
        for t in temp:
            d.append(int(t))
        data.append(d)
    fin.close()
    return data

def solve_one_case2(case):
    data=case
    data.sort()
    t_s=[]
    delta_t=0
    while data!=[1]*len(data):
        data.sort()
        t_s.append(data[-1]+delta_t)
        data=data[:-1]+[data[-1]/2,data[-1]-data[-1]/2]
        delta_t+=1
        t_s=[min(t_s)]
    if delta_t==0:
        return data[-1]
    else:
        return min(t_s)
        
def solve_recursively(data,t):
    data.sort()
    if max(data)<=3:
        return t+max(data)
    else:
        data1=[]
        for temp in data:
            if temp>1:
                data1.append(temp-1)
        if data[-1]!=9:
            data2=data[:-1]+[data[-1]/2,data[-1]-data[-1]/2]
        else:
            data2=data[:-1]+[6,3]
        t1=solve_recursively(data1,t+1)
        t2=solve_recursively(data2,t+1)
        return min((t1,t2))
    
def write_results2():
    data=read_data2()
    fout=open('output2.txt','w')
    for i in range(len(data)):
        result=solve_recursively(data[i],0)
        fout.write('Case #'+str(i+1)+': '+str(result)+'\n')
    fout.close()
        
        
        