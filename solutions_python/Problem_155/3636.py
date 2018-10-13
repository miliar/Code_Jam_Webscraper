text = open("aud.in", "rb")
n = int(text.readline().strip("\n"))
output = open("aud.out", "wb")
for i in range(n):
    line = text.readline().strip("\n")
    line = line.split()
    max = int(line[0])
    aud = [int(c) for c in line[1]]
    res = 0
    total = aud[0]
    for j in range(1, max + 1):
        if (aud[j] != 0 and j - total > 0):
            res += j - total
            total += res
        total += aud[j]
    output.write("Case #" + str(i + 1) + ": " + str(res) + "\n")
output.close()
text.close()
