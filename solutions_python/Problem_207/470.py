import sys

FILENAME = sys.argv[1]
# FILENAME = "sample_input.txt"

file = open(FILENAME)

T = int(file.readline().strip())

for i in range(T):
    N, R, O, Y, G, B, V = map(int, file.readline().strip().split())
    ans = ['' for _ in range(N)]
    t = {}
    if R > 0:
        t['R'] = R
    if Y > 0:
        t['Y'] = Y
    if B > 0:
        t['B'] = B

    j = 0
    if len(t) == 0:
        print "Case #" + str(i + 1) + ": " + ''.join(ans)
        continue
    col = max(t, key=t.get)
    while (j < N and (t[col] > 0)):
        ans[j] = col
        j += 2
        t[col] -= 1
        if t[col] == 0:
            del t[col]
            break
    if col in t or ans[0] == ans[N - 1]:
        ans = "IMPOSSIBLE"
        print "Case #" + str(i + 1) + ": " + ans
        continue
    # prev = None
    j = N - 1
    if len(t) == 0:
        print "Case #" + str(i + 1) + ": " + ''.join(ans)
        continue

    col = max(t, key=t.get)
    while (j >= 0 and (t[col] > 0)):
        if ans[j] != '':
            j -= 1
            # prev = None
            continue
        ans[j] = col
        j -= 2
        t[col] -= 1
        if t[col] == 0:
            del t[col]
            break
    if col in t or ans[0] == ans[N - 1]:
        ans = "IMPOSSIBLE"
        print "Case #" + str(i + 1) + ": " + ans
        continue

    j = 0
    if len(t) == 0:
        print "Case #" + str(i + 1) + ": " + ''.join(ans)
        continue

    col = max(t, key=t.get)
    while (j < N and (t[col] > 0)):
        if ans[j] != '':
            j += 1
            # prev = None
            continue
        ans[j] = col
        j += 2
        t[col] -= 1
        if t[col] == 0:
            del t[col]
            break
    if col in t or ans[0] == ans[N - 1]:
        ans = "IMPOSSIBLE"
        print "Case #" + str(i + 1) + ": " + ans
        continue
    print "Case #" + str(i + 1) + ": " + ''.join(ans)
