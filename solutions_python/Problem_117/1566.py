import sys

inFile = open(sys.argv[1], 'r')

outFile = open(sys.argv[1][:-2]+"out", "w")

number_of_input = int(inFile.readline().rstrip("\n"))

count = 0
flag = 1

while(count != number_of_input):
    order = inFile.readline().rstrip("\n").split()
    M = int(order[0])
    N = int(order[1])

    matrix = []
    for line in range(0,M):
        attrib = inFile.readline().rstrip("\n").split()
        matrix.append(attrib)

    count = count + 1

    if(M == 1 or N == 1):
        outFile.write("Case #%d: YES\n" % (count))
    else:
        flag = 1
        for r in range(0,M):
            LR = ''.join(matrix[r])
            
            if(LR.count("2") != N and LR.count("1") != N):
                for c in range(0,N):
                    if(LR[c] != "2"):
                        col = c
                        TB = ""
                        for k in range(0,M):
                            TB = TB + matrix[k][col]

                        if(TB.count("1") != M):
                            flag = 0;


        if(flag == 1):
            outFile.write("Case #%d: YES\n" % (count))
        else:
            outFile.write("Case #%d: NO\n" % (count))

inFile.close()
outFile.close()
