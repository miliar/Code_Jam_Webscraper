from bisect import bisect_right

for case in range(int(raw_input())):
    n = int(raw_input())
    a = sorted([float(i) for i in raw_input().split()])
    b = sorted([float(i) for i in raw_input().split()])

    w1 = 0
    w2 = 0
    # print a, b
    a1 = list(a)
    b1 = list(b)
    while True:
        if a1[len(a1) - 1] > b1[len(b1) - 1]:
            w1 += 1            
            del a1[len(a1) - 1]
        else:
            del a1[0]
        del b1[len(b1) - 1]
        if len(a1) == 0:
            break
    for i in range(n):
        p = bisect_right(b, a[i])
        if p == len(b):
            p -= 1
        if a[i] > b[p]:
            break
        b.remove(b[p])

    w2 = len(b)

    print "Case #" + str(case + 1) + ": " + str(w1) + " " + str(w2)