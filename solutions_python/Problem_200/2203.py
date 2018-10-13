data = open('b.in', 'r').readlines()
data = data[1:]


output = ""
for i in range(len(data)):
    line = str.strip(data[i])
    line = [int(x) for x in line]
    j = 0
    while j < len(line) - 1:
        if j > 0 and line[j - 1] > line[j]:
            j -= 1

        if line[j] > line[j + 1] and line[j] > 0:
            line[j] -= 1
            line[j + 1:] = [9] * len(line[j + 1:])
        elif line[j] > line[j + 1]:
            j -= 1
        else:
            j += 1

    number = "".join(map(str, line))
    output += "Case #{}: {}\n".format(i + 1, int(number))


f = open('b.out', 'w')
f.write(output)
