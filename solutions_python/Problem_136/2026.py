def solve_one(f):
    c, f, x = tuple([float(s) for s in f.readline().split()])
    cookie_rate, t = 2.0, 0.0
    while True:
        no_farm_time = x / cookie_rate
        farm_time = c / cookie_rate
        total_farm_time = farm_time + (x / (cookie_rate + f))
        if no_farm_time < total_farm_time:
            return t + no_farm_time
        else:
            cookie_rate += f
            t += farm_time

f = open("a.test", "r")
num_tests = int(f.readline())
for i in range(num_tests):
    print "Case #" + str(i+1) + ": " + ("%.7f" % solve_one(f))
