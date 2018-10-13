fin = open("input.txt", 'r')
fout = open("output.txt", "w")
c = int(fin.readline())
for i in range(c):
    firstAnswer = int(fin.readline())
    firstArr = []
    for j in range(4):
        row = list(map(int, fin.readline().split()))
        firstArr.append(row)
    secondAnswer = int(fin.readline())
    secondArr = []
    for j in range(4):
        row = list(map(int, fin.readline().split()))
        secondArr.append(row)
    row1 = firstArr[firstAnswer - 1]
    row2 = secondArr[secondAnswer - 1]
    ans = []
    for elem in row1:
        if elem in row2:
            ans += [elem]
    fout.write("Case #" + str(i + 1) + ": ")
    if len(ans) == 0:
        fout.write("Volunteer cheated!")
    elif len(ans) > 1:
        fout.write("Bad magician!")
    else:
        fout.write(str(ans[0]))
    fout.write("\n")
fin.close()
fout.close()

