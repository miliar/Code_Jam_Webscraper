'''
Magicka Trust
'''
def readInFile(path):
    t = 0
    with open(path,"r") as f:
        t =  int(f.readline())

        lines = f.readlines()
    return t,lines


def writeOutFile(path,data):
    with open(path,"w") as f:
        for i in range(len(data)):
            f.write("Case" + " #"+str(i+1) + ": " +str(data[i]).replace("'", '') + "\n")


def cal_moves(op,np):
    if np > op:
        return np - op                    
    else :
        return  op - np
    
def solve(data):
    results = []
    
    
    for line in data[1]:
        
        l = line.replace('\n','').split(' ')
       
        ltoInvoke = l[-1]
        
        c = int(l[0])
        Comb = []
        Comb_To = []
        for i in l[1:c+1]:
            z = [i[0],i[1]]
            z.sort()
            Comb.append(z)
            Comb_To.append(i[2])
            
        
        d = int(l[c+1])
        Opp = []
        for i in l[c+2:-2]:
            z = [i[0],i[1]]
            z.sort()
            Opp.append(z)
            
            
        elementList = []
        pE = ''
        print Comb
        print Comb_To
        print Opp
        print ltoInvoke
        print '+++'
        for e in ltoInvoke:
            print elementList
            
            if elementList : pE = elementList[-1]
            elementList.append(e)
            z = [pE,e]            
            z.sort()
            print z
            if z in Comb :
                eToAdd = Comb_To[Comb.index(z)]
                if elementList : elementList.pop()                
                if elementList : elementList.pop()
                elementList.append(eToAdd)
                print 
            print elementList    
                
            clearList = False
            for i in elementList[:-1]:
                z = [i,elementList[-1]]
                z.sort()
                if z in Opp : clearList = True
                
            if clearList : elementList = []

            
            
            print elementList
            
            
        results.append(elementList)
        
        
    return results

def main():
    data = readInFile("B-small-attempt2.in")
    results = solve(data)
    writeOutFile("B-small-attempt2.out",results)
    print "Done."
    print results


if __name__ == '__main__':
    main()