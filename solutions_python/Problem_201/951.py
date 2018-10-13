# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

t = int(raw_input())  # read a line with a single integer
for k in xrange(1, t + 1):
    N, K = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case

    S = {N:1}
    i = 0
    while i < K:
        cur_S = max(S.keys())

        L_s = (cur_S - 1) / 2
        R_s = cur_S / 2
        if S[cur_S] > K-1-i: break
        else:
            if R_s != 0:
                if R_s in S:
                    S[R_s] += S[cur_S]
                else:
                    S[R_s] = S[cur_S]
            if L_s != 0:
                if L_s in S:
                    S[L_s] += S[cur_S]
                else:
                    S[L_s] = S[cur_S]
            i += S[cur_S]
            S.pop(cur_S)

    print "Case #{}: {} {}".format(k, max(L_s, R_s), min(L_s, R_s))
    # check out .format's specification for more formatting options
