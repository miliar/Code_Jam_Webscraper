def read_data():
    fin=open('input.txt','r')
    flines=fin.readlines()
    fin.close()
    i=0
    T=int(flines[i])
    i+=1
    cases={}
    for t in range(1,T+1):
        cases[t]={}
        for g in (1,2):
            cases[t][g]=[]
            cases[t][g].append(flines[i][:-1])
            i+=1
            for l in range(4):
                cases[t][g].append(flines[i].split())
                i+=1
    return cases

def solve_for_case(case):
    ans1=int(case[1][0])
    ans2=int(case[2][0])
    line1=set(case[1][ans1])
    line2=set(case[2][ans2])
    answer = list(line1 & line2)
    if len(answer)==0:
        return 'Volunteer cheated!'
    elif len(answer)==1:
        return str(answer[0])
    else:
        return 'Bad magician!'

def run_1():
    cases=read_data()
    fout=open('output.txt','w')
    for i in cases.keys():
        answer=solve_for_case(cases[i])
        fout.write('Case #'+str(i)+': '+answer+'\n')
    fout.close()
    