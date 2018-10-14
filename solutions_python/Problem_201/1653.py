import sys
import math

inputName = "C-small-input.txt"

if (len(sys.argv)>1):
    inputName = sys.argv[1]

inFile = open(inputName, "rt")
outFile = open(inputName+".out", "wt")

T = int(inFile.readline())
for testCase in range(1, T + 1):
    outFile.write("Case #"+str(testCase)+": ")
    line = inFile.readline().strip().split()
    N = int(line[0])
    K = int(line[1])
    g_size=[]
    g_count=[]
    g_size.append(N)
    g_count.append(1)
    steps = int(math.log(K, 2))
#    print steps, " steps needed"
    for i in range(steps):
#        print "step ", i, " and the arrays are:"
#        print g_size
#        print g_count

        tmp_size = []
        tmp_count = []
        for j in range(len(g_size)):
            L = (g_size[j] - 1 ) / 2 
            R = (g_size[j] - 1 ) - L
            L_done = False
            R_done = False
            for k in range(len(tmp_size)):
                if (tmp_size[k] == L):
                    tmp_count[k] += g_count[j]
                    L_done = True
                if (tmp_size[k] == R):
                    tmp_count[k] += g_count[j]
                    R_done = True
            
            if (L_done == False):
                tmp_size.append(L)
                tmp_count.append(g_count[j])
            if (R_done == False):
                if (L == R):
                    tmp_count[-1] += g_count[j]
                else:
                    tmp_size.append(R)
                    tmp_count.append(g_count[j])

        g_size = tmp_size[:]
        g_count = tmp_count[:]

    g_size, g_count = zip(*sorted(zip(g_size, g_count), reverse=True))
    g_size = list(g_size)
    g_count = list(g_count)
#    print g_size
#    print g_count
    
    rest = K - (2**steps - 1)

    last_gap = g_size[0]
    index = 0
    while (rest > 0):
        g_count[index] -= 1
        last_gap = g_size[index]
        rest -= 1
        if (g_count[index] == 0):
            index += 1
        
        if (rest > 0) and ((index>len(g_count))or(g_size[index]<=0)):
            print "BAD ERROR!"

    L = (last_gap - 1 ) / 2 
    R = (last_gap - 1 ) - L
#    print "last person chooses a gap of ", last_gap," and so he will have: ", R," and ", L, " gaps on sides"
    
    outFile.write(str(R) + " " + str(L) + "\n")

inFile.close()
outFile.close()


