def output(t, res):
    casestr = "Case #" + str(t+1) +": "
    status = str(res) if res != None else "IMPOSSIBLE"
    outputLine = casestr+status
    print outputLine



def main():
    T = int( raw_input() )

    for t in xrange(T):
        S, K = raw_input().split(' ')
        K = int(K)
        S = [c == '+' for c in S]
        flips = 0
        for i in xrange(len(S)):
            if S[i]: continue

            if len(S) - i - K < 0:
                flips = None
                continue

            flips += 1
            for j in xrange(i, i+K):
                S[j] = not S[j]


        output(t, flips)


if __name__ == "__main__":
    main()