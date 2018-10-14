def magic(data, data2):
    num = []
    for i in data:
        if i in data2:
            num.append(i)
    if num == []:
        return "Volunteer cheated!"
    elif len(num) == 1:
        return num[0]
    else:
        return "Bad magician!"
test = open("A-small-attempt2.in", 'r')
outfile = open("MAGICIAN.DATA", 'w')
result = []
T = int(test.readline())
for j in range(1, T+1):
    row = int(test.readline())
    for i in range(1,5):
        arrangement = test.readline()
        if i == row:
            data = arrangement.split()
    row2 = int(test.readline())
    for i in range(1,5):
        arrangement = test.readline()
        if i == row2:
            data2 = arrangement.split()
    result.append("Case #" + str(j) + ": " + str(magic(data, data2)))
for i in result:
    outfile.write(i + '\n')
outfile.close()
test.close()

