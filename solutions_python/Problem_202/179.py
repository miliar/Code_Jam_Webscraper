def solve(N, models):
    A = models["+"]
    B = models["x"]
    C = models["o"]
    score = len(A) + len(B) + 2*len(C)

    A = A + C
    B = B + C
    
    addA = []
    addB = []
    addC =[]
    
    xB = [a for (a,b) in B]
    yB = [b for (a,b) in B]
    for i in range(1,N+1):
        for j in range(1,N+1):
            if i not in xB and j not in yB:
                addB.append((i,j))
                xB.append(i)
                yB.append(j)
                score += 1
    for i in addB:
        if i in A:
            addC.append(i)
            addB.remove(i)
    
    diag1 = [a+b for (a,b) in A]
    diag2 = [a-b for (a,b) in A]
    for i in (1,N):
        for j in range(1,N+1):
            if i+j not in diag1 and i-j not in diag2:
                addA.append((i,j))
                diag1.append(i+j)
                diag2.append(i-j)
                score += 1
                
    for i in addA:
        if i in B:
            addC.append(i)
            addA.remove(i)
        if i in addB:
            addC.append(i)
            addA.remove(i)
            addB.remove(i)
    
    add = len(addA) + len(addB) + len(addC)
    return (score, add, addA, addB, addC)
#%%

with open("in","r") as reader:
    with open("out",'w') as writer:
        t = int(reader.readline())
        for i in range(t):
            N, M = map(int,reader.readline().split())
            models = {"+":[], "x":[], "o":[]}
            for j in range(M):
                k, x, y = map(str, reader.readline().split())
                models[k].append((int(x), int(y)))
            score, add, addA, addB, addC = solve(N, models)
            writer.write("Case #" + str(i+1) + ": " + str(score) + " " + str(add) + "\n")
            for (a,b) in addA:
                writer.write("+ " + str(a) + " " + str(b) + "\n")
            for (a,b) in addB:
                writer.write("x " + str(a) + " " + str(b) + "\n")
            for (a,b) in addC:
                writer.write("o " + str(a) + " " + str(b) + "\n")