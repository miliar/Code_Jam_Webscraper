f = open('A-large.in.txt', 'r')
open('Aout.txt', 'w').close()
outFile = open('Aout.txt', 'w')

caseNum = int(f.readline())

for i in range(1, caseNum+1):
    inputs = f.readline().split()
    #print "case #", i, " input: ", inputs

    au = 0
    output = 0
    for s in range(int(inputs[0])+1):
        x = int(inputs[1][s])
        if x == 0:
            continue
        if au < s:
            output += (s - au)
            au = s
        au += x


    s = "Case #" + str(i) + ": " + str(output) + "\n"
    outFile.write(s)

    print s

