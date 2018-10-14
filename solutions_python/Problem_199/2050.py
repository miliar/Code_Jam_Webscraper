T = int(raw_input())

for t in xrange(T):
    S, K = raw_input().split(" ")
    K = int(K)

    arr = [0] * (len(S)+1)
    cumulative = [0] * (len(S)+1)
    flips = 0

    for i in xrange(len(S)-K+1):
        if i == 0:
            cumulative[i] = arr[i]
        else:
            cumulative[i] = arr[i] + cumulative[i-1]

        if (S[i] == '+' and cumulative[i] % 2 == 1) or (S[i] == '-' and cumulative[i] % 2 == 0):
            flips += 1
            arr[i] += 1
            arr[i+K] -= 1

        if i == 0:
            cumulative[i] = arr[i]
        else:
            cumulative[i] = arr[i] + cumulative[i-1]

    impossible = False
    for i in xrange(len(S)-K+1, len(S)):
        cumulative[i] = arr[i] + cumulative[i-1]
        if (S[i] == '+' and cumulative[i] % 2 == 1) or (S[i] == '-' and cumulative[i] % 2 == 0):
            impossible = True

    if impossible == True:
        print "Case #" + str(t+1) + ": IMPOSSIBLE"
    else:
        print "Case #" + str(t+1) + ": " + str(flips)