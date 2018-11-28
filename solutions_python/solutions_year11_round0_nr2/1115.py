infile = open("B.in")
outfile = open("B.out", "w")

for case in range(int(infile.readline())):
    line = infile.readline().split()
    print(str(case+1) + ": " + str(line))
    
    combinations = {}
    for k in line[1:1 + int(line[0])]:
        combinations[k[0:2]] = k[2]
        combinations[k[::-1][1:3]] = k[2]

    rejections = {}
    D_loc = 1 + int(line[0])
    D = int(line[D_loc])
    for k in line[D_loc + 1 : D_loc + D + 1]:
        rejections[k[0]] = k[1]
        rejections[k[1]] = k[0]

    invokations = line.pop()
    result = [invokations[0]]
    previous = invokations[0]
    for i in invokations[1:]:
        if previous + i in combinations:
            previous = combinations[previous + i]
            result[-1] = previous
        elif i in rejections and rejections[i] in result:
            result = []
            previous = "y"
        else:
            result.append(i)
            previous = i

    outfile.write("Case #" + str(case+1) + ": " + str(result).replace('\'', '') + "\n")

infile.close()
outfile.close()
