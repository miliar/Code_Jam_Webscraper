#A Magic Trick

fin = open("A-small-attempt0.in", "r")
fout = open("A-small-out.txt", "w")

for i in range(int(fin.readline())):
    x = int(fin.readline()) - 1
    for j in range(x):
        fin.readline()
    line1 = fin.readline().split()
    for j in range(4):
        line1[j] = int(line1[j])
    for j in range(3 - x):
        fin.readline()
        
    y = int(fin.readline()) - 1
    for j in range(y):
        fin.readline()
    line2 = fin.readline().split()
    for j in range(4):
        line2[j] = int(line2[j])
    for j in range(3 - y):
        fin.readline()
    C = 0
    asdf = 0
    for j in range(4):
        for k in range(4):
            if line1[j] == line2[k]:
                asdf = line1[j]
                C += 1
    if C == 0:
        Answer = "Volunteer cheated!"
    if C == 1:
        Answer = str(asdf)
    if C > 1 :
        Answer = "Bad Magician!"
    fout.write("Case #" + str(i + 1) + ": " + Answer + "\n")

fin.close()
fout.close()
