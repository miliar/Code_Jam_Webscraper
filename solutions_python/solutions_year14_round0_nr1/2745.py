f = open("small.in")
fout = open("ans.out", "w")
lines = f.readlines()

cases = int(lines[0])
counter = 1

for i in xrange(cases):
    col1 = int(lines[counter]) - 1
    counter += 1
    possible = set(lines[counter+col1].split())
    counter += 4
    col2 = int(lines[counter]) - 1
    counter += 1
    possible2 = set(lines[counter+col2].split())
    counter += 4
    intersection = possible & possible2
    fout.write("Case #" + str(i+1) + ": ")
    if len(intersection) == 1:
        fout.write(next(iter(intersection)) + "\n")
    elif len(intersection) == 0:
        fout.write("Volunteer cheated!\n")
    else:
        fout.write("Bad magician!\n")
    print intersection


fout.close()
f.close()
