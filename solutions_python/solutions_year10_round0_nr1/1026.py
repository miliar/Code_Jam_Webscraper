global snapper
def Zero(val):
    if val==0:
        return 0
    elif val==1:
        return 2
    elif val==2:
        return 2
    elif val==3:
        return 0

def One(val):
    if val==0:
        return 0
    elif val==1:
        return 2
    elif val==2:
        return 2
    elif val==3:
        return 0

def Two(val):
    if val==0:
        return 0
    elif val==1:
        return 2
    elif val==2:
        return 2
    elif val==3:
        return 0

def Three(val):
    if val==0:
        return 1
    elif val==1:
        return 3
    elif val==2:
        return 3
    elif val==3:
        return 1
        



def setSnapperValue(own,prev):
    if prev==0:
        return Zero(own)
    elif prev==1:
        return One(own)
    elif prev==2:
        return Two(own)
    else:
        return Three(own)
    



def update(sid):
    if sid>0:
        snapper[sid]=setSnapperValue(snapper[sid],update(sid-1))

        return snapper[sid]
    else:

        if snapper[0]==1:
            snapper[0]=3
        else:
            snapper[0]=1
    
        return snapper[0]




if __name__=="__main__":
    
    inp=open("A-small-attempt1.in","r")
    cases_inp=inp.readlines()
    cases=[]
    num_cases=int(cases_inp[0])
    for i in range(1,num_cases+1):
        case_str=cases_inp[i]
        els=case_str.split(' ')
        n=int(els[0])
        k=int(els[1])
        cases.append([n,k])
    
    inp.close()
    out=open("a.out","w")
    for c in range(0,num_cases):
        S=[1]
        for i in range(1,cases[c][0]):
            S.append(0)
        snapper=S
        k=0
        
        while k<cases[c][1]:
            update(cases[c][0]-1)
            k=k+1
        if snapper[cases[c][0]-1]==3:
            status="ON"
        else:
            status="OFF"

        out.write("Case #"+str(c+1)+": "+status+"\n")
    out.close()
         
