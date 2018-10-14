# Sean Liu
# Title

# FUNCTIONS



# IMPLEMENTATION

f = open("A-small-attempt1.in", "r")
g = open("output.txt", "w")

T = int(f.readline())

for i in range(T):

    numstrings = int(f.readline())
    strings = []

    for num in range(numstrings):
        strings.append(f.readline().split()[0])

    fegla = 0
    total = 0

    while ((fegla == 0) and (len(strings[0]) > 0)):
        letter = strings[0][0]
        letnums = []
        totnum = 0
        for stringnum in range(numstrings):
            letnum = 0
            pos = 0
            while (pos < len(strings[stringnum])) and (strings[stringnum][pos] == letter):
                letnum += 1
                pos += 1
            if (letnum == 0):
                fegla = 1
                break
            totnum += letnum
            letnums.append(letnum)
            strings[stringnum] = strings[stringnum][pos:]
        avg = round(totnum/numstrings)
        for x in letnums:
            total += abs(x-avg)

    for string in strings:
        if len(string) > 0:
            fegla = 1
            break

    if (fegla == 1):
        g.write("Case #{}: Fegla Won\n".format(i+1))
    else:
        g.write("Case #{}: {}\n".format(i+1, total))

f.close()
g.close()
