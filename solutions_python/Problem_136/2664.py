import sys

fname = sys.argv[1]

def close(x, y):
    return abs(x - y) < 1e-7

with open(fname) as f:
    prob = f.readlines()

kases = int(prob.pop(0))

for k in range(1, kases + 1):
    c, f, x = map(float, prob.pop(0).split(' '))
    t, r, y = 0.0, 2.0, 0
    while not close(x, y):
        time_needed_at_rate = (x - y) / r
        time_to_buy_farm = c / r
        time_needed_if_get_farm = time_to_buy_farm + (x - y) / (r + f)
        if time_needed_at_rate < time_needed_if_get_farm:
            t = t + time_needed_at_rate
            y = x
        else:
            t = t + time_to_buy_farm
            r = r + f
    print("Case #%d: %0.7f" % (k, t))
