def int2bin(n, count=24):
    return "".join([str((n >> y) & 1) for y in range(count-1, -1, -1)])

def all_are_on(n):
    x='y'
    for i in n:
        if i=='0':
            x='n'
    return x
#print int2bin(16)
#print int2bin(15)


infile = open("A-large.in","r")
outfile = open("A-large.out","w")
number_of_cases = int(infile.readline())
case = 1
while infile:
    string=infile.readline()
    if string=='':
        break
    l=string.split();
    N=int(l[0])
    K=int(l[1])
    
    state=int2bin(K,count=N)
    #print K,"=",int2bin(K,count=N)
    #print "state = ",state
    #if state == '0':
    #    s='OFF'
    #if state == '1':
    #    s='ON'
    if all_are_on(state)=='y':
        s='ON'
    else:
        s='OFF'
    outfile.write("Case #"+str(case)+": "+s+"\n")
    case = case+1
            
