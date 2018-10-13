inputs = []
outputs = []
path = 'B-small-attempt1.in'
#path = 'input.txt'
openFile = open(path, 'r')

inputsLen = int(openFile.readline())

for _ in range(inputsLen):
    inputs.append(openFile.readline()[:-1])
openFile.close()

for inp in inputs:
    if ''.join(sorted(inp)) != inp:
        index = len(inp)-1
        temp = inp
        while(''.join(sorted(str(temp))) != str(temp)):
            #print('inp : ' + temp)
            temp = temp[:index] + "9" + temp[index+1:]
            if(int(temp) > int(inp)):
                if(temp[0] == "1" and temp[index-1] == "0"):
                    temp = "09" + temp[2:]
                elif(temp[0] != "1" and temp[index-1] == "0"):
                    temp = str(int(temp[0])-1) + temp[1:]
                else:
                    temp = temp[:index-1] + str(int(temp[index-1])-1) + temp[index:]
            #print('out : ' + temp)
            index -= 1
        inp = temp
    outputs.append(inp)

path = 'output.out'
openFile = open(path, 'w')

for ind, out in enumerate(outputs):
    openFile.write("Case #" + str(ind+1) + ": " + str(int(out)) + "\n")

openFile.close()
