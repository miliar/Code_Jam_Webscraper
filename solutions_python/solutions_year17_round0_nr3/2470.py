__author__ = 'Vishal'

def stalls(n, k):
    # init stalls
    left_s = [x for x in xrange(n)]
    right_s = [n - 1 - x for x in xrange(n)]

    max_val = -10*n
    out_score = 0
    # choose spot
    for person in xrange(k):
        best_pos = -1
        best_score = (max_val, max_val)
        for x in xrange(len(left_s)):
            score = (min(left_s[x], right_s[x]), max(left_s[x], right_s[x]))
            if score > best_score:
                best_score = score
                best_pos = x
        # assign spot
        left_s[best_pos] = max_val
        right_s[best_pos] = max_val
        out_score = best_score
        # update nearby spots
        i = best_pos - 1
        while i > -1 and right_s[i] != max_val:
            right_s[i] = best_pos - i - 1
            i -= 1
        i = best_pos + 1
        while i < n and left_s[i] != max_val:
            left_s[i] = i - best_pos - 1
            i += 1
            if i == n:
                break
    return out_score

inp = map(lambda a: a.split(" "), open("C-small-1-attempt1.in").read().split("\n")[1:])
inp = [(int(x[0]), int(x[1])) for x in inp]

o = open("output.txt", "w")
for x in xrange(0, len(inp)):
    out = stalls(inp[x][0], inp[x][1])
    o.write("Case #" + str(x+1) + ": " + str(out[1]) + " " + str(out[0]) + "\n")
