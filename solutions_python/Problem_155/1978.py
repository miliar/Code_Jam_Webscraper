fin = open("A-large.in", "r")
fout = open("large.out", "w")

T = int(fin.readline())

for i in range(T):

    temp = fin.readline().split()
    Smax = int(temp[0])

    k = 0
    sumofs = 0
    for j in range(Smax + 1):
        if sumofs + k < j:
            k += j - (sumofs + k)
        sumofs += int(temp[1][j])

    fout.write("Case #%d: %d\n" % (i + 1, k))

fin.close()
fout.close()
        
    
