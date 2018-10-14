import pdb
import time
import math

def decompose(n,m):
    o = []
    for i in range(m):
        if (n/(2**i))%2==1:
            o.append(1)
        else:
            o.append(0)
    return o

def subprocess(f,caseNum,f2):
    #============== data ================

    cands = []
    candsBin = []

    #=============== loading ============
    start_loading = time.clock()

    noC = int(f.readline())
    #print "number of candies : ",noC

    ss = f.readline().split()
    for s in ss:
        cands.append(int(s))

    cands.sort()

    #print "cands:",cands

    #print "loading time : ", time.clock() - start_loading
    #pdb.set_trace()

    #============== process =============
    start_process = time.clock()

    if len(cands)<=1:
        print "imposible!!!"
        f2.write("Case #"+str(caseNum+1)+": ")
        f2.write("NO")
        f2.write("\n")
        return True

    maxS = int(math.log(max(cands),2))+1
    #print "maxS:",maxS

    for c in cands:
        candsBin.append(decompose(c,maxS))

    #print "candsBin:",candsBin

    for i in range(maxS):
        s = sum([cb[i] for cb in candsBin])
        #print "i:",i," s:",s
        if (s%2)!=0:
            print "imposible!!!"
            f2.write("Case #"+str(caseNum+1)+": ")
            f2.write("NO")
            f2.write("\n")
            return True

    bestScore = sum(cands[1:])
        
    print "process time : ", time.clock() - start_process
    
    print "=============="
    
    #==================

    f2.write("Case #"+str(caseNum+1)+": ")

    f2.write(str(bestScore))
    
    f2.write("\n")
    
    return True

def process(inputFile,outputFile):
    print "process ",inputFile
    f = open(inputFile,"r")
    f2 = open(outputFile,"w")
    noCase = int(f.readline())
    print "number of cases : ",noCase
    for c in range(noCase):
        print "case : ",c+1,"/",noCase
        r = subprocess(f,c,f2)
        if not r:
            print "!!!force stop!!!"
            break
    f.close()
    f2.close()

def main():
    path = "D:\\home\\mathieu\\googleJam\\Qualification\\"
    inputFile = path+"C-large.in"
    outputFile = path+"C-large.out"
    process(inputFile,outputFile)
    print "done"

if __name__ == "__main__":
    main()
