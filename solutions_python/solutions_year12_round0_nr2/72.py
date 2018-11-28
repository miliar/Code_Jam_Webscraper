#!/usr/bin/python
# Filename: Problem B. Dancing With the Googlers.py

#file = "Problem B. Dancing With the Googlers"
file = "Problem B. Dancing With the Googlers A-small-attempt0(1)"
#file = "Problem B. Dancing With the Googlers A-large-attempt0"


#debug = True
debug = False

def solve(instr):
    data = instr.split()
    
    if debug:
        print(data)
        
    for i in range(len(data)):
        data[i] = int(data[i])
        
    if debug:
        print(data)
        
    ret = 0
    normal = 0
    sprprise = 0
    
    nGooglers = data.pop(0)
    nSurprising  = data.pop(0)
    p = data.pop(0)
    
    if debug:
        print("nGooglers {},nSurprising {},p {}:\n".format(nGooglers ,nSurprising,p))

    for i in range(len(data)):
        remainder = data[i]%3
        x = data[i] // 3

        if debug:
            print("x,remainder:\n")
            print(x)
            print(remainder)
    
        if 0 == remainder:
            if x >= p:
                normal += 1
            elif(x - 1 >0 and x+1 >= p):
                sprprise += 1
        elif 1 == remainder:
            if x+1 >= p:
                normal += 1
        elif 2 == remainder:
            if x+1 >= p:
                normal += 1
            elif x+2 >= p:
                sprprise += 1
        else:
            print("error\n")
        
        if debug:
            print("normal,sprprise:\n")
            print(normal)
            print(sprprise)
            
    ret += normal

    if(sprprise >= nSurprising):
        ret += nSurprising
    else:
        ret += sprprise
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


