import sys

it = (e.strip() for e in  sys.stdin)

for i in range(int(it.next())):
    P, K, L = [int(e) for e in it.next().split(" ")]
    freqs = sorted([int(e) for e in it.next().split(" ")])[::-1]
    assert P * K >= L 
    total = sum(freq*(cnt/K+1) for freq, cnt in zip(freqs, range(len(freqs))))
    print "Case #%i: %i" % (i+1, total)
        
    
    