T = int(raw_input())

for t in range(T):
    s = raw_input().split(' ')
    smax = int(s[0])
    aud = s[1]
    max_needed = 0
    current_sum = 0
    for i in range(smax+1):
        needed = 0
        if current_sum < i:
            needed = i - current_sum
            max_needed += needed
        current_sum += int(aud[i])+needed
    print "Case #%d: %d"%(t+1,max_needed)
