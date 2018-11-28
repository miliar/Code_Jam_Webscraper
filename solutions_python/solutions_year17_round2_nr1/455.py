def parse(fi):
    f = open(fi,"r")
    return map(lambda x: x[:-1],f.readlines())

def p1():
    i = 1
    data = parse("problem1/input.txt")
    for count in range(int(data[0])):
        dest = int(data[i].split()[0])
        maxhours = 0
        for num in range(int(data[i].split()[1])):
            i += 1
            maxhours = max(maxhours,(dest - float(int(data[i].split()[0])))/float(int(data[i].split()[1])))
        i += 1
        print "Case #" + str(count + 1) + ": " + str(round(float(dest)/float(maxhours),6))


p1()
