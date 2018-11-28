import math
input = open("input.txt","r")    
output = open("output.txt","w+")
cases = int(input.readline())

for case in range(1,cases+1):
    print("--")
    l,p,c = map(int,input.readline().split())
    val = 0
    fac = math.ceil((p-l)/l)
    print(fac)
    val = math.floor(math.log(fac)/math.log(c))
    if(val>0):
        out = math.floor(math.log(val,2))+1
    else:
        out = 0
    output.write("Case #%d: %d\n"%(case,out))