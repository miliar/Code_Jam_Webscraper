inFile = open("RecycledNums.in", "r")
outFile = open("RecycledNums.out", "w")

T = int(inFile.readline().strip())

def count(A, B):
    total = 0
    for n in xrange(A, B+1):
        for m in xrange(n+1, B+1):
            if isRecycled(str(n), str(m)):
                total += 1
    return total

def isRecycled(n, m):
    found = False
    i = len(n) -1
    while not found and i > 0:
        new = n[i:] + n[:i]
        if new == m: found = True
        i-=1
    return found


for case in range(1, T+1):
    A, B = inFile.readline().strip().split()
    A = int(A)
    B = int(B)
    ans = count(A, B)
    out = "Case #%s: %s" %(case, ans)
    outFile.write(out + "\n")

outFile.close()