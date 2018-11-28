inFile = open("B-large.in.in", 'r')
outFile = open("magicka.out",'w')
N = int(inFile.readline())
for i in range(1,N+1):
    line = inFile.readline().split()
    c = int(line[0])
    combinations = {}
    for j in range(1,c+1):
        # parse combinations
        combinations[line[j][0:2]] = line[j][2]
        combinations[line[j][1]+line[j][0]] = line[j][2]
    d = int(line[c+1])
    oppositions = {x:[] for x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    for j in range(c+2, c+2+d):
        # parse oppositions
        oppositions[line[j][0]].append(line[j][1])
        oppositions[line[j][1]].append(line[j][0])
    string = line[-1]
    output = ''
    for char in string:
        output += char
        if len(output) > 1:
            if output[-2:] in combinations:
                output = output[:-2] + combinations[output[-2:]]
            else:
                for c in output:
                    if c in oppositions[char]:
                        output = ''
                        break
    
    outStr = '['
    if len(output) > 0:
        for j in range(len(output)-1):
            outStr += output[j]+", "
        outStr += output[-1]+']'
    else:
        outStr += ']'
    outFile.write("Case #"+str(i)+": "+outStr+"\n")
    print("Case #"+str(i)+": "+outStr)
