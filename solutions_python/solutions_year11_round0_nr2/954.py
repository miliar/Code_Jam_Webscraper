f=file('B-large.in','r')
inp=[]
for line in f:
    if '\n' in line:
        line=line[:-1]
    inp.append(line)
f.close()

f=file('something.out','w')

N=int(inp[0])
inp=inp[1:]

casenum=1

for case in inp:
    temp=[]
    case=case.split(' ')
    Cn=int(case[0])
    C={}
    for i in range(1,Cn+1):
        t=case[i]
        C[t[:2]]=t[-1]
        C[t[:2][::-1]]=t[-1]
    case=case[Cn+1:]

    Dn=int(case[0])
    D=[]
    for i in range(1,Dn+1):
        t=case[i]
        D.append(t)
        D.append(t[::-1])
    case=case[Dn+1:]

    L=int(case[0])
    elist=case[1]

    for i in range(0,L):
        letter=elist[i]
        temp.append(letter)
        ind=len(temp)
        if ind>1:
            if temp[ind-2]+letter in C.keys():
                temp.insert(ind-2,C[temp[ind-2]+letter])
                temp=temp[:ind-1]
            else:
                for k in temp:
                    for j in temp[1:]:
                        if k+j in D:
                            temp=[]
                            break
    string='['
    for n, letter in enumerate(temp):
        if n==len(temp)-1:
            string=string+letter
        else:
            string=string+letter+', '
    string=string+']'
    f.write('Case #%i: %s\n'%(casenum,string))
    casenum+=1
f.close()
print 'Done'
