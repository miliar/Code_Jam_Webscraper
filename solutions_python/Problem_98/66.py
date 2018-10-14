#!/usr/bin/python
# Filename: Problem D. Hall of Mirrors.py

file = "Problem D. Hall of Mirrors small"


#debug = True
debug = False

def solve(inFile):
    instr = inFile.readline()
    data = instr.split()
    assert 3 == len(data)
    H = int(data[0])
    W = int(data[1])
    D = int(data[2])

    MyX = 0
    MyY = 0
    
    for i in range(H):
        rowStr = inFile.readline()
        for j in range(W):
            if "X" == rowStr[j]:
                MyY = i
                MyX = j
                break

    W -= 2
    Dx0 = MyX - 0.5
    Dx1 = W - Dx0

    H -= 2
    Dy0 = MyY - 0.5
    Dy1 = H - Dy0

    if debug:
        print(H,W,D,Dx0,Dx1,Dy0,Dy1)
        
    n = 1
    ret = 0

    n0 = 0
    n1 = 0
    n2 = 0
    n3 = 0
    
    while(1):
        cont = 0
        
        D0 = 2*(n//2)*H + 2*(n%2)*Dy0
        if(D0 > D):
            if 0 == n0:
                n0 = n
            cont += 1
            
        D2 = 2*(n//2)*W + 2*(n%2)*Dx1
        if(D2 > D):
            if  (0 == n1):
                n1 = n
            cont += 1
            
        D4 = 2*(n//2)*H + 2*(n%2)*Dy1
        if(D4 > D):
            if 0 == n2:
                n2 = n
            cont += 1

        D6 = 2*(n//2)*W + 2*(n%2)*Dx0
        if(D6 > D):
            if 0 == n3:
                n3 = n
            cont += 1
            
        if(4 == cont):
            break
        n += 1


    if debug:
        print(n0,n1,n2,n3)

    if n0 > 1:
        ret += 1
    if n1 > 1:
        ret += 1
    if n2 > 1:
        ret += 1
    if n3 > 1:
        ret += 1

    a0 = []
    if(n0>1 and n1>1):
        for i in range(1,n0):
            for j in range(1,n1):
                D0 = 2*(i//2)*H + 2*(i%2)*Dy0
                D1 = 2*(j//2)*W + 2*(j%2)*Dx1
                if((D0**2 + D1**2)**0.5 <= D):
                    if D0/D1 not in a0:
                        ret += 1
                        a0.append(D0/D1)
                else:
                    break
    a1 = []
    if(n1>1 and n2>1):
        for i in range(1,n2):
            for j in range(1,n1):
                D0 = 2*(i//2)*H + 2*(i%2)*Dy1
                D1 = 2*(j//2)*W + 2*(j%2)*Dx1
                if((D0**2 + D1**2)**0.5 <= D):
                    if D0/D1 not in a1:
                        ret += 1
                        a1.append(D0/D1)
                else:
                    break
    a2 = []
    if(n3>1 and n2>1):
        for i in range(1,n2):
            for j in range(1,n3):
                D0 = 2*(i//2)*H + 2*(i%2)*Dy1
                D1 = 2*(j//2)*W + 2*(j%2)*Dx0
                if((D0**2 + D1**2)**0.5 <= D):
                    if D0/D1 not in a2:
                        ret += 1
                        a2.append(D0/D1)
                else:
                    break
    a3 = []
    if(n3>1 and n0>1):
        for i in range(1,n0):
            for j in range(1,n3):
                D0 = 2*(i//2)*H + 2*(i%2)*Dy0
                D1 = 2*(j//2)*W + 2*(j%2)*Dx0
                if((D0**2 + D1**2)**0.5 <= D):
                    if D0/D1 not in a3:
                        ret += 1
                        a3.append(D0/D1)
                else:
                    break
    return (ret)

def main():
    inFile = open(file+".in")
    assert inFile
    outFile = open(file+".out",'w')
    assert outFile
    
    T = int(inFile.readline())
    print(T)
    for n in range(T):
        soln = solve(inFile)
        print ("Case #%d: %s\n" % (n+1, soln))
        outFile.write("Case #{0}: {1}\n".format(n+1, soln));
        
    inFile.close()
    outFile.close()

main()

