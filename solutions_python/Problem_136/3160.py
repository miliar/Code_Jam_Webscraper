__author__ = 'diana fisher'

def IsApproximatelyEqual(x, y, epsilon):
    """Returns True iff y is within relative or absolute 'epsilon' of x.

    By default, 'epsilon' is 1e-6.
    """
    # Check absolute precision.
    if -epsilon <= x - y <= epsilon:
        return True

    # Is x or y too close to zero?
    if -epsilon <= x <= epsilon or -epsilon <= y <= epsilon:
        return False

    # Check relative precision.
    return (-epsilon <= (x - y) / x <= epsilon
            or -epsilon <= (x - y) / y <= epsilon)


filename = "B-large.in"
inputFile = open(filename, "r")
lines = []
for line in inputFile:
    lines.append( line.strip() )

inputFile.close()

numCases = int(lines[0])
# print 'num cases = ', numCases

for i in range(1, numCases+1):
    # print '----------------------------------------------------'
    case = "Case #" + str(i) + ":"
    line = lines[i]
    values = line.split()
    C = float(values[0])  # Cost of cookie farm.
    F = float(values[1])  # When you buy a farm, it costs you C cookies and gives you F cookies/sec
    X = float(values[2])  # When you have X cookies not spent on farms, you win.

    # print 'C:', C, "F:", F, "X:", X

    num_cookies = 0         # start with 0 cookies
    production = 2.0         # cookies/sec
    time = 0

    seconds_until_farm = C / production
    # print 'seconds_until_farm:', seconds_until_farm

    max_seconds = X / production     # the number of seconds to reach X without purchasing any farms
    # print 'max_seconds:', max_seconds

    t1 = time + max_seconds
    t2 = time + seconds_until_farm

    # print 't1:', t1, "t2:", t2

    while (True):

        # purchase farm..
        time += seconds_until_farm
        production += F

        # print 'time:', time
        # print 'production:', production

        max_seconds = X / production
        # print 'max_seconds:', max_seconds

        seconds_until_farm = C / production
        # print 'seconds_until_farm:', seconds_until_farm

        previousT1 = t1
        t1 = time + max_seconds
        t2 = time + seconds_until_farm

        # print 't1:', t1, "t2:", t2
        if (previousT1 < t1):
            print case, previousT1
            break