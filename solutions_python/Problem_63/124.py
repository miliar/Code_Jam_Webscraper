
i = open("in.txt", "r")
o = open("out.txt", "w")

Tests = int(i.readline())
for test in range(Tests):
    line = i.readline()
    l = int(line.split()[0])
    p = int(line.split()[1])
    c = int(line.split()[2])

    x=0
    while l*c<p:
        c = c*c
        x = x + 1

    res = x;
    o.write("Case #{0}: {1}\n".format(test+1, res))

o.close()
i.close()
