def read_data1():
    fin=open('A-large.in','r')
    flines=fin.readlines()
    data=[]
    for i in range(1,len(flines)):
        temp=flines[i].split()
        data.append(temp[1])
    fin.close()
    return data
    
def solve_one_case(case):
    total=0
    friend_needed=0
    for i in range(len(case)):
        if total==i and case[i]=='0':
            total+=1
            friend_needed+=1
        else:
            total+=int(case[i])
    return friend_needed
    
def write_results():
    fout=open('output1.txt','w')
    data=read_data1()
    for i in range(len(data)):
        case=data[i]
        fn=solve_one_case(case)
        fout.write('Case #'+str(i+1)+': '+str(fn)+'\n')
    fout.close()