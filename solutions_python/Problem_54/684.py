 
def gcd(a,b):
    while (b != 0):
        t = b
        b = (a % b)
        a = t
    return a

def makeInt(list):
    i=0
    max = 0 
    min=10**50
    for x in list:
        x =int(x)
        if(x>max):
            max = x
        if(x<min):
            min = x
        list[i] = x
        i=i+1
    return (list[0],list[1:],max,min)
        

def compute_result(list):
    (N,list,max,min) = makeInt(list)

    g = 0
    for x in list:
        list = list [1:]
        for y in list:
            z = abs(x-y)
            g = gcd(g,z)            

    if((max%g)==0):
        return 0
    d = max/g
    return abs((d+1)*g -max)

   
infile=open("B-large.in")     
outfile = open("B-large.out","w")

y = 0

C = int(infile.readline())
cases = 1
while(cases <= C):
    inStr  = infile.readline()
    list = inStr.split()

    y = compute_result(list)

    outStr = "Case #%d: %d\n" %(cases,y)
    outfile.write(outStr)
    cases = cases+1
