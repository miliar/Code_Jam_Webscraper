myfile = open("C-small-attempt4.in.txt", "r")
output = open("output.txt", "w")
import math

cases = int(myfile.readline())


for x in range(1, cases+1):
    count =0
    (lower, upper) = map(int, myfile.readline().split())
    possible =[]
    lm = int((math.sqrt(lower)))-1
    um = int(math.floor(math.sqrt(upper)))+1
    for i in range(lm, um+1):
        if (str(i**2)==str(i**2)[::-1]) and str(i)==str(i)[::-1] and (lower<=i**2<=upper):
            count+=1
    out = "Case #%d: " %(x) +str(count)
    output.write(out+"\n")
        
        
myfile.close()
output.close()
