import heapq as hq

t = int(raw_input())
for ti in range(t):
    n,k = map(int, raw_input().split())
    stoll = [0] * n

    q = [(len(stoll), 0, stoll)]
    while k > 0:
        q.sort(key=lambda x: x[1])
        q.sort(key=lambda x: -x[0])

        for _ in range(len(q)):
            ln, left, s = q.pop(0)
            i = (ln-1) / 2

            s1 = s[:i]
            ln_s1 = len(s1)
            left_s1 = left

            s2 = s[i+1:]
            ln_s2 = len(s2)
            left_s2 = left + i + 1

            if ln_s1 > 0: q.append((ln_s1, left_s1, s1))
            if ln_s2 > 0: q.append((ln_s2, left_s2, s2))

            k -= 1
            if k == 0:
                maxlr = ln - i - 1
                minlr = i
                print "Case #%s: %s %s" % (ti+1, maxlr, minlr)
                break
        if k == 0: break
