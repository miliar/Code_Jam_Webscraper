T = int(raw_input())
for tt in range(T):
    Ps,K = raw_input().split(" ")
    K = int(K)
    Ps = list(Ps)
    counter = 0
    for i,c in enumerate(Ps):
        if c == '-' and i+K <= len(Ps):
            counter += 1
            for j in range(i,i+K):
                if Ps[j] == '-':
                    Ps[j] = '+'
                else:
                    Ps[j] = '-'
    for c in Ps:
        if c == '-':
            counter = -1
    if counter >= 0:
        print "Case #" + str(tt+1) + ": " + str(counter)
    else:
        print "Case #" + str(tt+1) + ": IMPOSSIBLE"


