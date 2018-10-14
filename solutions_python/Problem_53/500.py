def calcsnap(n, k):
    if (k + 1) % (2 ** n) == 0:
        return "ON"
    else:
        return "OFF"

infile = open("A-large.in.txt")
outfile = open("A-large.out.txt", "w")

cases = int(infile.readline())

for i in range(1, cases + 1):
    n, k = infile.readline().rstrip("\n").split(" ")
    outfile.write("Case #" + str(i) + ": " + calcsnap(int(n), int(k)) + "\n")

outfile.close()
