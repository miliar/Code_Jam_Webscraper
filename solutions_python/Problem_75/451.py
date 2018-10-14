import pdb
import time

def check_combine(o,combs):
    lo = len(o)
    for i in range(lo):
        for c in combs:
            if o[i]==c[0] and i+1<lo and o[i+1]==c[1]:
                return (i,c[2])
            if o[i]==c[1] and i+1<lo and o[i+1]==c[0]:
                return (i,c[2])
    return None

def check_fusion(o,ops):
    for os in ops:
        if os[0] in o and os[1] in o:
            return True
    return False

def subprocess(f,caseNum,f2):
    #============== data ================

    combs = []
    ops = []
    inv = []
    output = []

    #=============== loading ============
    start_loading = time.clock()

    ss = f.readline().split()
    cur = 0

    # number of combinaisons
    noC = int(ss[cur])
    cur = cur + 1
    #print "noC:",noC,

    for i in range(noC):
        combs.append((ss[cur][0],ss[cur][1],ss[cur][2]))
        cur = cur + 1

    # number of opositions
    noO = int(ss[cur])
    cur = cur + 1
    #print "noO:",noO,

    for i in range(noO):
        ops.append((ss[cur][0],ss[cur][1]))
        cur = cur + 1

    # number of invokation
    noI = int(ss[cur])
    cur = cur + 1
    #print "noI:",noI
    
    for i in range(noI):
        inv.append(ss[cur][i])
    cur = cur + 1

    #print "loading time : ", time.clock() - start_loading
    #pdb.set_trace()

    #print "noC:",noC
    #print "noO:",noO
    #print "noI:",noI

    #print "combs:",combs
    #print "ops:",ops
    #print "inv:",inv

    #============== process =============
    start_process = time.clock()

    for iv in inv:
        output.append(iv)

        #print "output1:",output

        while True:
            cc = check_combine(output,combs)
            #print "cc:",cc
            if cc==None:
                break
            #print "combinaison"
            output[cc[0]:(cc[0]+2)] = []
            output.insert(cc[0],cc[1])
            #print "output4:",output
            
        #print "output2:",output
        
        cf = check_fusion(output,ops)
        #print "ff:",cf
        if cf:
            output = []

        #print "output3:",output

    #print "process time : ", time.clock() - start_process
    
    #print "=============="
    
    #==================

    f2.write("Case #"+str(caseNum+1)+": ")

    f2.write("[")
    for i in range(len(output)):
        if i!=0:
            f2.write(", ")
        f2.write(output[i])
    f2.write("]")
    
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
    inputFile = path+"B-large.in"
    outputFile = path+"B-large.out"
    process(inputFile,outputFile)
    print "done"

if __name__ == "__main__":
    main()
