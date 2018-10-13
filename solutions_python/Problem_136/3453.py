import sys

with open(sys.argv[1]) as input:
    ts = int(input.readline())
    for test in range(ts):
        row = input.readline().split()
        [cost, farm, xp] = map(float, row)
        cf = 2.0
        total = 0.0
        while True:
            if xp / cf > (cost / cf + xp / (cf + farm)):
                total += cost / cf
                cf = cf + farm
            else:
                break
        
        print "Case #%d: %.7f" %(test+1, total + xp/cf)
