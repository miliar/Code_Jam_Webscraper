t = int(raw_input())

for i in xrange(1, t + 1):
    s, k = raw_input().split(" ")
    s = [c is '+' for c in s]
    l = len(s)
    k = int(k)
    flip_end = [False] * len(s)
    flip = False
    count = 0

    for j in xrange(0, l):
        if j <= l - k and not s[j] ^ flip:
            flip_end[j + k - 1] = True
            flip = not flip
            count += 1
        elif not s[j] ^ flip:
            count = -1
            break
        if flip_end[j]:
            flip = not flip

    if count >= 0:
        print "Case #{}: {}".format(i, count)
    else:
        print "Case #{}: IMPOSSIBLE".format(i)
