from sys import stdin

T = int(stdin.readline().strip())
for i in range(T):
    line = stdin.readline().strip().split(' ')
    s_max = int(line[0])
    s = list(line[1])
    s = [int(j) for j in s]
    assert(s_max+1 == len(s))
    sums = [0]
    cnt = 0
    for j in range(0, s_max):
        sums.append(sums[j] + s[j])
    for j in range(s_max, 0, -1):
        if j <= sums[j]:
            continue
        else:
            cnt = max(j - sums[j], cnt)
    print "Case #{}: {}".format(i+1, cnt)
