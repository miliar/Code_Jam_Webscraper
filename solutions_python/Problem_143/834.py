import sys
import random

inp = open("input.txt","r")
out = open("outpuut.txt","w")

def main():
    nCases = int(inp.readline())
    output = []
    for case in range(nCases):
        row = map(int,inp.readline().split())
        a = row[0]
        b = row[1]
        c = row[2]

        andlist = []
        
        for i in range(a):
            for j in range(b):
                andlist.append(i&j)

        count = 0
        for s in andlist:
            if s< c:
                count+=1

        






               
        output.append("Case #"+str(case+1)+": "+str(count))
            
    for case in range(nCases):
        #print output[case]
        out.write("{0}\n".format(output[case]))


    

if __name__ == '__main__':
    
    try:
        import psyco
        psyco.full()
    except ImportError:
        pass     
    main()
    inp.close()
    out.close()
