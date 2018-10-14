f = open('A-small-attempt3.in', 'r')
out = open('output', 'w')
nbcase = f.readline()
for j in range(int(nbcase)):
    shymax = f.read(1)
    print (shymax)
    f.read(1)
    s = f.readline()
    i = 0
    tab = []
    for c in s:
        if c != '\n':
            tab.append(int(c))
    shyreach = 0
    friends = 0
    i = 0
    for e in tab:
        if shyreach >= i:
            shyreach += tab[i]
        else:
            tmp = i - shyreach
            friends += tmp
            shyreach += tmp + tab[i] #
        i += 1


    print("shyreach = ", shyreach)
    out.write("Case #{0}: {1}\n".format(j+1, friends))

