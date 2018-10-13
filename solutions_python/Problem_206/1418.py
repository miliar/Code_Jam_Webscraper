inputs = []
outputs = []

path = 'A-large.in'
#path = 'input.txt'
openFile = open(path, 'r')
inputLen = int(openFile.readline())

for _ in range(inputLen):
    line = openFile.readline().split(" ")
    others = []
    for _ in range(int(line[1])):
        other_line = openFile.readline().split(" ")
        others.append([int(other_line[0]), int(other_line[1])])
    inputs.append([int(line[0]), int(line[1]), others])
openFile.close()

#print(inputs)

for i in range(inputLen):
    times = []
    for j in range(inputs[i][1]):
        times.append((inputs[i][0] - inputs[i][2][j][0])/inputs[i][2][j][1])
    min_time = times.index(max(times))

    outputs.append(inputs[i][0]/times[min_time])



path = 'output.out'
openFile = open(path, 'w')
for ind, output in enumerate(outputs):
    openFile.write("Case #" + str(ind+1) + ": " + "{:.6f}".format(round(output, 6)) + "\n")
openFile.close()
