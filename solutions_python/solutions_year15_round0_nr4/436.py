myinf = "sample.txt"

myinf = "D-small-attempt0.in"
#myinf = "B-large-practice.in"

#myout = open("output.txt",'wt')
myout = open("output1.txt",'wt')
#myout = open("output2.txt",'wt')

#import sys
#sys.setrecursionlimit(2000)

myin = open(myinf,'rt').read().split('\n')
num_case = int(myin[0])
print(num_case)
for i in range(num_case):
    #if just uses 1 line per case
    shift=i+1
    inputs = myin[shift].split()
    in_ints = [int(x) for x in inputs]  #for ints
    #in_floats = [float(x) for x in inputs] #fot floats
    X=in_ints[0]
    R=in_ints[1]
    C=in_ints[2] 

    if X==1:
        myout.write("Case #%d: %s\n"%((i+1),"GABRIEL"))
    elif X==2:
        if (R*C)%2:
            myout.write("Case #%d: %s\n"%((i+1),"RICHARD"))
        else:
            myout.write("Case #%d: %s\n"%((i+1),"GABRIEL"))
    elif (X>6) or (X>max(R,C)) or (X//2>=min(R,C)) or (X>R*C) or (R*C)%X!=0 or (X>=5 and min(R,C)<=2) or (min(R,C)==2 and X==4):
        myout.write("Case #%d: %s\n"%((i+1),"RICHARD"))

    else:
        myout.write("Case #%d: %s\n"%((i+1),"GABRIEL"))
    
myout.close()    
