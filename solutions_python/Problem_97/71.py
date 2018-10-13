#!/usr/bin/python
# Filename: Problem C. Recycled Numbers.py

#file = "Problem C. Recycled Numbers"
#file = "Problem C. Recycled Numbers A-small-attempt0"
file = "Problem C. Recycled Numbers A-large-attempt0"


debug = True
#debug = False

def subSolve(n,B):
    nStr = str(n)
    wide = len(nStr)
    ret = 0

    mlist = []
    for moving in range(wide):
        mStr = nStr[-moving:] + nStr[:-moving]
        m = int(mStr)
        if(m>n and m<=B):
            if m not in mlist:
                mlist.append(m)
                ret += 1
    return ret


def solve(instr):
    data = instr.split()
    
    if debug:
        print(data)
        
    for i in range(len(data)):
        data[i] = int(data[i])

    
    A = data[0]
    B = data[1]
    
    ret = 0
    for i in range(A,B):
        ret += subSolve(i,B)
        
    return (ret)

def main():
    inFile = open(file+".in")
    assert inFile
    outFile = open(file+".out",'w')
    assert outFile
    
    T = int(inFile.readline())
    print(T)
    for n in range(T):
        soln = solve(inFile.readline())
        if debug:
            print ("Case #%d: %s\n" % (n+1, soln))
        outFile.write("Case #{0}: {1}\n".format(n+1, soln));
        
    inFile.close()
    outFile.close()

main()

