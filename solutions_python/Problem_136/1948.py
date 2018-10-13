import sys
lines = open(sys.argv[1] + ".in", "rU").read().split("\n")

outfile = open(sys.argv[1] + ".out", "w")

for i, test in enumerate(lines[1:]):
    if not test:
        break
    c, f, x = map(float, test.split())
    time = 0
    rate = 2
    smallest = float('inf')
#    print("new test case")
    while time < smallest:
#        print("buying", i, "time", time + x / rate, "zeroed at", time)
        smallest = min(smallest, time + x / rate)
        time += c / rate
        rate += f
    print("Case #{}: {}".format(i+1, smallest), file=outfile)
