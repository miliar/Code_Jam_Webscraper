def check(a,b):
    inter = a & b
    l = len(inter)
    if (l == 1):
        return str(inter.pop())
    elif (l > 1):
        return "Bad magician!"
    else:
        return "Volunteer cheated!"

f = open("A-small-attempt0.in", 'r')

n = int(f.readline().strip())
for i in range(n):
    tmp = int(f.readline().strip())
    for j in range(4):
        tmp -= 1
        l = f.readline().strip()
        if (not tmp):
            a = set([int(x) for x in l.split(" ")])
    tmp = int(f.readline().strip())
    for j in range(4):
        tmp -= 1
        l = f.readline().strip()
        if (not tmp):
            b = set([int(x) for x in l.split(" ")])
    print "Case #%d: %s" % (i+1, check(a,b))