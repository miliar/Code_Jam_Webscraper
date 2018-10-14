import sys

fi = open(sys.argv[1], "r")
fo = open("out", "w")

char = fi.read(1)
buf = ""
while char != '\n':
    buf += char
    char = fi.read(1)
T = int(buf)

for i in range (1, T + 1):
    Smax = fi.read(1)
    fi.read(1)
    char = fi.read(1)
    buf = ""
    while char != '\n' and char != '':
        buf += char
        char = fi.read(1)

    S = []
    for x in list(buf):
        S.append(int(x))
    n = 0
    friends = 0
    for j, s in enumerate(S):
        if n < j:
            friends += j - n
            n += j - n
        n += s
    output = "Case #{0}: {1}".format(i, friends)
    print output
    fo.write(output)
    if i != T:
        fo.write("\n")
        
    
    
