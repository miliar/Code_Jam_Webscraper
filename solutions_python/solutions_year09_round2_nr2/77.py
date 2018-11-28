from sys import stdin
from sys import stdout

for case in range(1, int(stdin.readline()) + 1):
    s = stdin.readline().strip()
    counts = [0] * 10
    for ch in s:
        counts[int(ch)] = counts[int(ch)] + 1
    j = 0
    for i in range(len(s)-1, 0, -1):
        if s[i] > s[i-1]:
            j = i
            break;

    if j == 0:
        for i in range(1, 10):
            if counts[i] > 0:
                min = i
                break
        r = [str(min)]
        counts[min] = counts[min] - 1
        counts[0] = counts[0] + 1
        for i in range(0, 10):
            for k in range(counts[i]):
                r.append(str(i))
    else:
        k = j
        while k < len(s) - 1 and s[k+1] > s[j-1]: k = k + 1
        r = [ch for ch in s]
        t = r[k]
        r[k] = r[j-1]
        r[j-1] = t

        r[j:] = sorted(r[j:])
    print "Case #%d: %s" % (case, "".join(r))