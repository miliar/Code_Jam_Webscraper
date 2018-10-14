#problemA
       

def problemA(fileName):
    f = open(fileName,'r')
    testNum = int( f.readline())


    output = open("Output.txt",'w')
    
    for i in range(testNum):
        s = f.readline().split()
        d,n = float(s[0]),int(s[1])
        
        t = 0
        for ii in range(n):
            ss = f.readline().split()
            dd, nn = float(ss[0]),float(ss[1])

            tt = (d - dd)/nn
            t = max(t,tt)
        res = d/t
                
        output.write("Case #"+ str(i+1) +": "+str(res))
        output.write("\n")

import time
if __name__ == '__main__':
    t=time.time()
    problemA("A-large.in.txt")
    print(time.time()-t)
    print("Complete")
