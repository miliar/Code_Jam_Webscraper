import sys

if len(sys.argv) < 2:
    print "Usage: a.py input"
    exit()

input = sys.argv[1]
f = open(input)
T = f.readline()
T = int(T)

if T < 1 or T > 20:
    print "T is out of range"
    exit()

for i in range(T):
    s = f.readline().strip("\n").split(" ")
    N = int(s[0])
    ss = [0] * N
    ts = [0] * N
    ms = [0.0] * N
    judge_sum = 0
    for k in range(N):
        ss[k] = int(s[k + 1])
        judge_sum += ss[k]

    avg = judge_sum * 2 / N
    guaranteeds_sum = 0
    guaranteeds = 0

    for s in ss:
        if s > avg:
            guaranteeds += 1
            guaranteeds_sum += s

    attainable_avg = 1.0*(2*judge_sum - guaranteeds_sum) / (N - guaranteeds)

    for j in range(N):
        to_avg = attainable_avg - ss[j]
        if to_avg < 0:
            to_avg = 0
        ts[j] = to_avg
        ms[j] = to_avg * 1.0 / judge_sum * 100

    print "Case #%d:" % (i + 1),
    for m in ms:
        print "%f" % (m),
    print
