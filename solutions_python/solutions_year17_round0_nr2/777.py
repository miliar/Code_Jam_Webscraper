import fileinput

for t, l in enumerate(list(fileinput.input())[1:]):
    # Detect first decrease from left to right
    l = [int(i) for i in l.strip()]
    for i in range(len(l) - 1):
        if (l[i + 1] < l[i]):
            # Ripple changes back to the start
            leftmostChange = None
            for j in range(i + 1, 0, -1):
                if (l[j] < l[j - 1]):
                    l[j - 1] = l[j - 1] - 1
                    leftmostChange = j - 1
            for j in range(leftmostChange + 1, len(l)):
                l[j] = 9
    # Trim any potential zero padding
    l = ''.join(map(str, l))
    print "Case #{}: {}".format(t + 1, l.lstrip('0'))
