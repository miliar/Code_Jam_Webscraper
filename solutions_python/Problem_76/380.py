

def S(a,b):
    return a^b
def sum(a,b):
    return a+b
def Reduce(S1,bro):
    if len(bro)==0:
        return 0
    else:
        return reduce(S1,bro)
    
T=input()
for loop in range(1,T+1):
    
    N=input()

    line_list=raw_input().split()

    Big_bro=[int(x) for x in line_list]

    Big_bro=sorted(Big_bro)
    Small_bro=[]
    check=0
    
    while (len(Big_bro)>0):
        Small_bro.append(Big_bro.pop(0))
        
        if Reduce(S,Big_bro) == Reduce(S,Small_bro):
            print "Case #%d: %d" % (loop,Reduce(sum,Big_bro))
            check=1
            break        
    
    if check==0:
        print "Case #%d: NO" %loop
