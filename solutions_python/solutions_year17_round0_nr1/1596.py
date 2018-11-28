import sys

inputName = "A-large-input.txt"

if (len(sys.argv)>1):
    inputName = sys.argv[1]

inFile = open(inputName, "rt")
outFile = open(inputName+".out", "wt")

T = int(inFile.readline())
for testCase in range(1, T + 1):
    outFile.write("Case #"+str(testCase)+": ")
    line = inFile.readline().strip().split()
    S = list(line[0])
    K = int(line[1])
    if (not ('-' in S)):
        outFile.write("0\n")
        continue
    tries = 0
    for j in range (len(S)-K+1):
        if (S[j]=='+'):
            continue
        tries += 1
        for k in range(K):
            if (S[j+k])=='-':
                S[j+k]='+'
            elif (S[j+k]=='+'):
                S[j+k]='-'

    if ('-' in S):
        outFile.write("IMPOSSIBLE\n")
        continue
    else:
        outFile.write(str(tries)+"\n")
        continue

inFile.close()
outFile.close()


