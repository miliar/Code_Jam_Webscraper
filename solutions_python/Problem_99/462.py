f=open('A-small-attempt0.in')
T=int(f.readline().strip())
def get_prob(State, A, P):
    p = 1.0
    for i in range(A):
        p *= P[i] if(State[i]=='0') else (1-P[i])
    return(p)
def get_ks(State, A, B, bksp):
    ks = B-A+(bksp*2)+1

    if(bksp > A): return(B+2)
    elif('1' not in State):
        return(B-A+(bksp*2)+1)
    elif(bksp != 0):
        r = 0
        if('1' in State[:-bksp]):
            r += (ks+B+1)
        else:
            r += ks
        return(r)
        #~ State=State[:-bksp]
        #~ if('1' not in State):
            #~ return(B-A+(bksp*2)+1)
    else:
        if('1' in State):
            return(ks+B+1)

for case in range(T):
    A, B = ( int(x) for x in f.readline().strip().split() )
    P = [ float(x) for x in f.readline().strip().split() ]
    #~ R = { bin(i)[2:].zfill(A):get_probablity(bin(i)[2:].zfill(A), P) for i in range(2**A) }
    R = 10000
    Plist  = [ get_prob(bin(i)[2:].zfill(A), A, P) for i in range(2**A)]
    for bksp in range(A+2):
        Kslist = [ get_ks(bin(i)[2:].zfill(A), A, B, bksp) for i in range(2**A) ]
        x = 0
        for p,k in zip(Plist,Kslist):
            x += (p*k)
        if(x < R):  R=x
    print('Case #%d: %0.6f'%(case+1,R))