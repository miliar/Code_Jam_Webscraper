inputs = []
outputs = []
#path = 'input.txt'
path = 'C-small-1-attempt1.in'
openFile = open(path, 'r')

inputsLen = int(openFile.readline())

for _ in range(inputsLen):
    temp = openFile.readline().split(" ")
    inputs.append([int(temp[0]), int(temp[1])])
openFile.close()

for inp in inputs:
    gaps = [inp[0]]
    add = 1
    for _ in range(inp[1]-1):
        max_index = gaps.index(max(gaps))
        maxValue = gaps[max_index]
        del(gaps[max_index])
        if(maxValue % 2 == 0):
            gaps.append(maxValue//2-1)
            gaps.append(maxValue//2)
        else:
            gaps.append(maxValue//2)
            gaps.append(maxValue//2)

    max_index = gaps.index(max(gaps))
    maxValue = gaps[max_index]
    if(maxValue % 2 == 0):
        dist = [maxValue//2-1, maxValue//2]
    else:
        dist = [maxValue//2, maxValue//2]

    outputs.append([max(dist), min(dist)])

path = 'output.out'
openFile = open(path, 'w')

for ind, out in enumerate(outputs):
    openFile.write("Case #" + str(ind+1) + ": " + str(out[0]) + " " + str(out[1]) + "\n")

openFile.close()
