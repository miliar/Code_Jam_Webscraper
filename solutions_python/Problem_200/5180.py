def getLast(n):
    last = n
    nm = n
    f = False
    while not f:
        l = [int(d) for d in str(nm)]
        for index, j in enumerate(l):
            if len(l) == 1:
                last = nm
                f = True
                break
            if index != len(l)-1:
                if j > l[index+1]:
                    break
                else:
                    last = nm
            else:
                f = True
        nm -= 1
    return last


x = int(raw_input())
lasts = []
cases = []
for i in range(x):
    case = int(raw_input())
    cases.append(case)
    lasts.append(getLast(case))

for index_, k in enumerate(cases):
    print "Case #%d: %d" % (index_+1, lasts[index_])