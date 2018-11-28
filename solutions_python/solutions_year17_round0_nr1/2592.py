def flip(ch):
    return '+' if ch == '-' else '-'

f = open('out.out','w')
n = int(raw_input())
for cNum in xrange(1, n + 1):
    seq, k = raw_input().split(" ")
    seq = list(seq)
    k = int(k)
    times = 0
    for i in range(len(seq)- k + 1):
        if seq[i] == '-':
            times += 1
            for j in range(k):
                seq[i + j] = flip(seq[i + j])
            #print seq
    isfinished = True
    for i in range(len(seq) - k, len(seq)):
        if seq[i] == '-':
            isfinished = False
            break
    if isfinished:
        f.write("Case #" + str(cNum) + ": " + str(times) + '\n')
    else:
        f.write("Case #" + str(cNum) +": IMPOSSIBLE\n")

            