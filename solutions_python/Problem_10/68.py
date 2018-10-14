source = "A-large"
sin = source+".in"
sout = source+".out"

txt = open(sin).readlines()
txt = [x.strip() for x in txt]

txt.pop(0)

cases = []
while txt:
    P, K, L = [int(x) for x in txt.pop(0).split()]
    freq = [(n, int(x)) for (n, x) in enumerate(txt.pop(0).split())]
    cases.append((P,K,L,freq))


f = open(sout, "w")

for num, (P,K,L,freq) in enumerate(cases):
    print num, P, K, L, freq
    answer = "Case #%d: " % (num+1)
    if L > P*K:
        answer += "Impossible"
    else:
        keys = {}
        for key, fr in freq:
            keys[key] = fr
        print keys
        print

        keys = sorted([x[::-1] for x in keys.items()])
        keys.reverse()

        keys = [x[1] for x in keys]

        pad = {}
        for i in xrange(K):
            pad[i] = []

        while keys:
            for i in xrange(K):
                if keys:
                    pad[i].append( keys.pop(0) )

        total = 0
        for key, times in freq:
            for i in xrange(K):
                if key in pad[i]:
                    total += (pad[i].index(key)+1)*times
        answer += str(total)

    f.write(answer+"\n")
    print answer

f.close()
