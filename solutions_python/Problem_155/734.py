

f = open("A-large.in", 'r')

n = int(f.readline())

for x in xrange(n):
    line = f.readline()
    splited = line.split(" ");
    maxLevel = int(splited[0])

    need = 0
    level = 0
    curnum = 0
    for level in xrange(maxLevel+1):
        num = int(splited[1][level])
        if (curnum >= level):
            curnum = num + curnum
        else:
            need = need + level - curnum
            curnum = curnum + num + level - curnum
    print "Case #" + str(x+1) + ": " + str(need)
