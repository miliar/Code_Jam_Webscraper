fin = file("A-small-attempt0.in", "rU")
fout = file("A-small.out", "w")

gdict = {'a': 'y', 'b': 'h', 'c': 'e', 'd': 's', 'e': 'o', 'f': 'c',
         'g': 'v', 'h': 'x', 'i': 'd', 'j': 'u', 'k': 'i', 'l': 'g',
         'm': 'l', 'n': 'b', 'o': 'k', 'p': 'r', 'q': 'z', 'r': 't',
         's': 'n', 't': 'w', 'u': 'j', 'v': 'p', 'w': 'f', 'x': 'm',
         'y': 'a', 'z': 'q'}

nruns = int(fin.readline().strip())
for i in xrange(nruns):
    line = fin.readline().strip()

    result = ''

    for lett in line:
        if lett != ' ':
            result += gdict[lett]
        else:
            result += ' '

    strout = "Case #" + str(i+1) + ": " + str(result) + "\n"
    print strout
    fout.write(strout)
fin.close()
fout.close()
