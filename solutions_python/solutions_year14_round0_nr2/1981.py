import sys

fd = open(sys.argv[1])

case = int(fd.readline().strip())
for n in xrange(1, case + 1):
    c, f, x = [ float(i) for i in fd.readline().strip().split() ]
    r = 2.0
    ans = 0.0

    time_to_x_1 = x / r
    wait_to_buy_time = c / r
    time_to_x_2 = wait_to_buy_time +  ( x / ( r + f ) )

    while time_to_x_1 > time_to_x_2:
        ans += wait_to_buy_time
        r += f

        wait_to_buy_time = c / r
        time_to_x_1 = x / r
        time_to_x_2 = wait_to_buy_time +  ( x / ( r + f ) )

    ans += time_to_x_1

    print "Case #%d: %.7f"%(n, ans)
