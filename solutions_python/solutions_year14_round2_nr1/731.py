def reduce_strings(strings):
    new_strings=[]
    c=strings[0][0]
    counts=[]
    for i in range(len(strings)):
        string=strings[i]
        count=0
        if len(string)>0:
            while string[0]==c:
                string=string[1:]
                count+=1
                if len(string)==0:
                    break
        counts.append(count)
        new_strings.append(string)
    return c,counts,new_strings

def create_reduce_dict(strings):
    chars=[]
    string_dict={}
    n=0
    while len(strings[0])>0:
        c,counts,strings = reduce_strings(strings)
        
        chars.append(c)
        string_dict[n]=counts[:]
        n+=1
    for string in strings:
        if len(string)>0:
            chars.append('X')
            string_dict[n]=[0]
    return chars,string_dict

def solve_for_case(strings):
    chars, string_dict=create_reduce_dict(strings)
    steps=0
    for i in range(len(chars)):
        counts=string_dict[i]
        best=sum(counts)/len(counts)
        for count in counts:
            if count==0:
                return 'Fegla Won'
            steps+=abs(best-count)
    return str(steps)

def read_data():
    fin=open('input.txt','r')
    flines=fin.readlines()
    fin.close()
    T=int(flines[0])
    N=0
    t=0
    strings=[]
    cases={}
    for i in range(1,len(flines)):
        if N==0:
            N=int(flines[i])
            cases[t]=strings
            strings=[]
            t+=1    
        else:
            strings.append(flines[i].split()[0])
            N-=1
    cases[t]=strings
    return cases, T

def solve_1B():
    cases,T=read_data()
    fout=open('output.txt','w')
    for i in range(1,T+1):
        print i
        answer=solve_for_case(cases[i])
        fout.write('Case #'+str(i)+': '+answer+'\n')
    fout.close()
            
           

           