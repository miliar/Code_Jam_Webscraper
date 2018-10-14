tests = []

def best_time((c, f, x)):
    remaining = x-c
    time = 0
    rate = 2.0
    buy = True
    while (buy):
        ty = x / (rate + f)
        tn = remaining / rate
        if (ty > tn):
            time += x/rate
            buy = False
        else:
            time += c/rate
            rate += f
    return time

f = open("B-large.in", 'r')
n = int(f.readline().strip())
for i in range(n):
    param = f.readline().strip().split(" ")
    tests.append((float(param[0]), float(param[1]), float(param[2])))
for i in range(n):
    print "Case #%d: %.7f" % (i+1, best_time(tests[i]))

# Test Cases
# 30.0 1.0 30.0     for C = X