def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:
        a, b = b, a % b
    return a

import math
fo = open("A-small-attempt0.in")
fo2 = open("output.txt", mode='w')
tests = eval(fo.readline())
output = []
for x in range(1,tests+1):
    str1 = fo.readline().strip("\n")
    str1=str1.split("/")
    p=eval(str1[0])
    q=eval(str1[1])
    result=math.ceil(math.log(q/p,2))
    if (result<(1/math.pow(2,40))):
        result=-1

    gcd1=gcd(q,p);
    p=p/gcd1;
    q=q/gcd1;
    if(math.log(q,2)!=math.ceil(math.log(q,2))):
        result=-1;
        #print("f-not 2")
    #print(result)
    if(result==-1):
        output.append("Case #"+str(x)+": impossible"+"\n")
    else:
        output.append("Case #"+str(x)+": "+str(result)+"\n")




fo2.writelines(output)
