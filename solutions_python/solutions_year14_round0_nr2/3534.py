import sys

lines = [line.strip() for line in sys.stdin.readlines()]
test_cases = int(lines.pop(0))

def read_values():
    line = lines.pop(0)
    return (float(n) for n in line.split())


def analyze():
    def time_for_x(c, f, x, farms=0, cps=2.0):
        farm_time = 0.0
        while farms > 0:
            farms -= 1
            farm_time += c / cps
            cps += f
        return farm_time + x / cps

    C, F, X = read_values()

    farms = 0
    time = time_for_x(C, F, X, farms)
    while True:
        next_time = time_for_x(C, F, X, farms + 1)
        if time <= next_time: break
        time = next_time
        farms += 1

    return time

for test_case in range(test_cases):
    time = analyze()
    print 'Case #%s: %s' % (test_case + 1, time)
