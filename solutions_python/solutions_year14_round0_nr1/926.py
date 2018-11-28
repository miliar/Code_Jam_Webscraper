def main():
    t = int(raw_input())
    for i in range(1, t + 1):
        c = test()
        print "Case #%d: %s" % (i, c)



def test():
    a1 = int(raw_input())
    b1 = []
    for i in range(0, 4):
        b1.append([int(x) for x in raw_input().split()])
    a2 = int(raw_input())
    b2 = []
    for i in range(0, 4):
        b2.append([int(x) for x in raw_input().split()])
    l = intersect(b1[a1-1],b2[a2-1])
    if len(l) == 0:
        return 'Volunteer cheated!'
    elif len(l) > 1:
        return 'Bad magician!'
    else:
        return str(l[0])



def intersect(a, b):
     return list(set(a) & set(b))

main()