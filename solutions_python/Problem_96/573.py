import sys
import string

if len(sys.argv) < 2:
    print "Usage: $(basename $0): input"
    exit()

input = sys.argv[1]
f = open(input)
T = f.readline()
T = int(T)

if T < 1 or T > 100:
    print "T out of range"
    exit()

N_max = 100

def max_normal(N):
    return (N + 2) / 3

def max_surprising(N):
    if N >= 2 and N <= 28:
        return (N + 4) / 3
    if N < 2:
        return 0
    if N > 28:
        return 10

# if t_i % 3 == 1, then max_normal == max_surprising
# otherwise, max_normal + 1 = max_surprising

def googlers_surpassing(S, p, t):
    surpassing = 0
    surprises_left = S
    for t_i in t:
        t_i = int(t_i)
        if max_normal(t_i) >= p:
            surpassing += 1
        elif surprises_left > 0 and max_surprising(t_i) >= p:
            surprises_left -= 1
            surpassing += 1
    return surpassing

for i in range(T):
    s = f.readline().strip("\n").split(" ")
    N = int(s[0])
    S = int(s[1])
    p = int(s[2])
    t = s[3:3+N]

    if N < 1 or N > N_max:
        print "N out of range"
        exit()

    if S < 0 or S > N:
        print "S out of range"
        exit()

    if p < 0 or p > 10:
        print "p out of range"
        exit()

    for t_i in t:
        t_i = int(t_i)

        if t_i < 0 or t_i > 30:
            print "t_i out of range"
            exit()

    surpassers = googlers_surpassing(S, p, t)
    print "Case #%d: %d" % (i + 1, surpassers)
