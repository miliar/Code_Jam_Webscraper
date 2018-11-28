c = int(raw_input())
for case in range(1, c+1):
    n, k = map(int, raw_input().split())
    if (k+1) % 2**n == 0:
        print "Case #%d: ON" % case
    else:
        print "Case #%d: OFF" % case

