def flipping(S, k, d):
    global res, cake_dict
    if S not in cake_dict or cake_dict[S] > d:
        cake_dict[S] = d
    else:
        return

    if '-' not in S:
        res.append(d)
    for i in range(len(S)-k+1):
        if '-' in S[i:i+k]:
            flip = ""

            for c in S[i:i+k]:
                if c == '-': flip += '+'
                else: flip += '-'

            flipping(S[:i] + flip + S[i+k:], k, d+1)

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    S, k = raw_input().split(" ")  # read a list of integers, 2 in this case
    k = int(k)

    cake_dict = {}
    res = []
    flipping(S, k, 0)
    if res:
        res = min(res)
    else:
        res = "IMPOSSIBLE"
    print "Case #{}: {}".format(i, res)
    # check out .format's specification for more formatting options
