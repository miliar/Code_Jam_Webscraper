import sys

n_tests = int(sys.stdin.readline())
for i in range(n_tests):
    price, extra_gain, target = tuple([float(x) for x in sys.stdin.readline().split()])
    t, r = 0, 2
    #print(price, extra_gain, target)

    # Keep gaining cookies until can buy a farm, until which time
    # check if buying the farm will make you better off, if not, then
    # break loop
    while True:
        t += price / r
        
        # Check if remaining time is less than the time
        # needed to start over, if so, don't buy
        if (target - price) / r < target / (r+extra_gain):
            t += (target-price)/r
            break
        else:
            r += extra_gain
    print("Case #" + str(i+1) + ": " + str(t))
