def isTidy(s):
    for i in range(len(s)-1):
        if s[i] > s[i+1]: return False
    return True

t = int(input())
for caseN in range(1, t+1):
    s = input()
    ts = '%s'  % s
    ptr = len(ts) - 1
    if len(ts) == 1 or isTidy(ts) is True:
        print("Case #%d: %d" % (caseN, int(s)))
        continue

    while ptr >= 0:
        if ptr == 0:
            l = len(ts)-1
            ts = '9' * l
            print("Case #%d: %d" % (caseN, int(ts)))
            break
        if ts[ptr-1] > ts[ptr]:
            ts = ts[:ptr-1] + str(int(ts[ptr-1]) - 1) + ts[ptr:]
            for i in range(ptr, len(ts)):
                ts = ts[:i] + '9' + ts[i+1:]
            if isTidy(ts) is True:
                k = int(ts)
                while isTidy(str(k)) is True:
                    k += 1
                print("Case #%d: %d" % (caseN, k-1))
                break
        ptr -= 1
