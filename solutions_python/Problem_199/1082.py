infile = open("A-large.in", "r")
outfile = open("Aout.txt", "w")

tcase = int(infile.readline().rstrip())
for z in range(1, tcase+1):
    inline = infile.readline().rstrip()
    pancakes, size = inline.split()
    pancakes = list(pancakes)
    size = int(size)
    count = 0
    for i in range(0, len(pancakes) - size + 1):
        if pancakes[i] == "-":
            for j in range(i, i+size):
                if pancakes[j] == "+":
                    pancakes[j] = "-"
                else:
                    pancakes[j] = "+"
            count+=1
    allup = True
    for i in range(0, len(pancakes)):
        if pancakes[i] == "-":
            allup = False
    if allup == True:
        outfile.write("Case #" + str(z) + ": " + str(count) +"\n")
    else:
        outfile.write("Case #" + str(z) + ": IMPOSSIBLE\n")

outfile.close()
infile.close()
