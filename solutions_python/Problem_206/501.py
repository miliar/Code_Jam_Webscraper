def output(t, res):
    casestr = "Case #" + str(t+1) +": "
    status = str(res) if res != None else "IMPOSSIBLE"
    outputLine = casestr+status
    print outputLine



def main():
    T = int( raw_input() )

    for t in xrange(T):
        D, N = map(int, raw_input().split(' '))
        slowest = 0
        for n in xrange(N):
            K, S = map(int, raw_input().split(' '))
            time = (D - K)* 1.0/S
            slowest = max(slowest, time)
        output(t, D*1.0/slowest)


if __name__ == "__main__":
    main()