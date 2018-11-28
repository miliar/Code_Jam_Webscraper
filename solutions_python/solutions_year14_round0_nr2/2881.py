import sys

def optimal(time_offset, rate, target, cost, rate_inc):
    wait = time_offset + target / rate;
    last = wait + 1

    new_time = time_offset
    new_rate = rate

    while last > wait:
        last = wait
        new_time = new_time + cost /  new_rate
        new_rate = new_rate + rate_inc

        wait = new_time + target / new_rate

    # No longer getting any better
    return last

def main():
    cases = int(sys.stdin.readline())
    i = 0

    while i < cases:
        line = sys.stdin.readline().strip()
        cost, rate, target = map(float, line.split(' '))

        result = optimal(0, 2, target, cost, rate)

        print 'Case #%d: %s' % (i + 1, '{0:.7f}'.format(result))
        i += 1

main()
