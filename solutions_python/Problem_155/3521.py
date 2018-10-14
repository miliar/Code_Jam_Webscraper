file = open('A-small-attempt0.in.txt', 'r')

T = int(file.readline())
output = ""

for i in range(0, T):
    case = file.readline()

    sMax = int(case[:1])
    string = case[2:]
    array = [] * sMax

    for c in string:
        array.append(c)

    count = 0
    audience = 0

    for j in range(0, len(array) - 1):
        while audience < j:
            count += 1
            audience += 1

        audience += int(string[j])
    
    output += "Case #" + str(i + 1) + ": " + str(count) + "\n"

fileOutput = open('output.txt', 'w')
fileOutput.write(output)
fileOutput.close()

file.close()
