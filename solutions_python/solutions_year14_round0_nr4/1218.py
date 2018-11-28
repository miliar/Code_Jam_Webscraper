filein = open("PD.txt", "r")
out = open("PDout.txt", "w")
cases = int(filein.readline())
for i in xrange(cases):
    numblocks = int(filein.readline())
    A = filein.readline().split()
    B = filein.readline().split()
    A.sort()
    B.sort()
    C = A[:]
    D = B[:]
    score1 = 0
    score2 = 0
    for j in xrange(numblocks):
        cur = C[0]
        win = True
        for k in xrange(len(D)):
            if float(D[k])> float(cur):
                win = False
                C = C[1:]
                D = D[0:k]+D[k+1:]
                break

        if win:
            score2 += 1
            C = C[1:]
            D = D[1:]
    C = A[:]
    D = B[:]
    for j in xrange(numblocks):
        cur = C[0]
        if float(cur) > float(D[0]):
            score1 +=1
            C = C[1:]
            D = D[1:]
        else:
            C = C[1:]
            D = D[:len(D)]
    out.write("Case #" + str(i+1) + ": " + str(score1) + " " + str(score2) +"\n")
    
filein.close()
out.close()

        
