import sys

inputName = "B-large-input.txt"

if (len(sys.argv)>1):
    inputName = sys.argv[1]

inFile = open(inputName, "rt")
outFile = open(inputName+".out", "wt")

T = int(inFile.readline())
for testCase in range(1, T + 1):
    outFile.write("Case #"+str(testCase)+": ")
    line = inFile.readline().strip()
    num = list(line)
    step_value = 0
    step_index = 0
    for i in range(len(num)):
        digit = int(num[i])
        if (digit>step_value):
            step_value=digit
            step_index=i
            continue

        if (digit==step_value):
            continue

        if (digit<step_value):
            for j in range(step_index + 1, len(num)):
                num[j]='9'
            num[step_index] = str(step_value - 1)
            break

    if (num[0] != '0'):
        outFile.write(num[0])
    for i in range(1, len(num)):
        outFile.write(num[i])
        
    outFile.write("\n")

inFile.close()
outFile.close()


