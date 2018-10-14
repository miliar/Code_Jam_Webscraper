for t in range(int(raw_input())):
    n, k = [int(i) for i in raw_input().split()]
    print "Case #" + str(t+1) + ':',
    if bin(k)[-n:].count('1') == n: print "ON"
    else: print "OFF"

