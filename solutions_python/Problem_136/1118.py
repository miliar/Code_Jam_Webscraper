def calculate_n(C,F,X):
    n=(X*F-2*C-C*F)/(C*F)
    return n

def calculate_time(C,F,X):
    n=calculate_n(C,F,X)
    n_f=0
    time=0.0
    while n_f<n:
        time+=C/(2+n_f*F)
        print time
        n_f+=1
    time+=X/(2+n_f*F)
    return round(time,7)

def read_data():
    fin=open('input.txt','r')
    flines=fin.readlines()
    fin.close()
    T=int(flines[0])
    cases=[]
    for c in range(1,T+1):
        cases.append(flines[c].split())
    return cases
    
def run_2():
    cases=read_data()
    fout=open('output.txt','w')
    for i in range(len(cases)):
        C,F,X = cases[i]
        C=float(C)
        F=float(F)
        X=float(X)
        time=calculate_time(C,F,X)
        fout.write('Case #'+str(i+1)+': '+str(time)+'\n')
    fout.close()