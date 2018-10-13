from sys import stdin, stderr

def deceitfulwar(a, b):
    points = 0
    a = a[:]
    b = b[:]
    while len(a) > 0:
        if min(a) < min(b):
            itema = min(a)
            itemb = max(b)
        elif max(a) > max(b):
            itemb = max(b)
            itema = min([x for x in a if x > itemb])
        else:
            itema = min(a)
            itemb = max(b)
        if itema > itemb:
            points += 1
        a.remove(itema)
        b.remove(itemb)
    return points

def regularwar(a, b):
    points = 0
    a = a[:]
    b = b[:]
    while len(a) > 0:
        itema = max(a)
        tmp = [x for x in b if x > itema]
        if len(tmp) > 0:
            itemb = min(tmp)
        else:
            itemb = min(b)
        if itema > itemb:
            points += 1
        a.remove(itema)
        b.remove(itemb)
    return points

for i in range(int(stdin.readline())):
    case = i + 1
    numblocks = int(stdin.readline())
    blocks1 = map(float, stdin.readline().split())
    blocks2 = map(float, stdin.readline().split())
    
    points1 = deceitfulwar(blocks1, blocks2)
    points2 = regularwar(blocks1, blocks2)

    print "Case #{:}: {:} {:}".format(case, points1, points2)
