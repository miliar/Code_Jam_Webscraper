"""
3
2525 1
2400 5

300 2
120 60
60 90

100 2
80 100
70 10
"""


def calculate_speed(d, n):
    horses = list()
    for j in xrange(0, n):
        k_and_s = raw_input()
        k = int(k_and_s.split(" ")[0])
        s = int(k_and_s.split(" ")[1])
        horses.append((k, s))

    if n == 1:
        k = horses[0][0]
        s = horses[0][1]
        time_taken = float(d - k)/s
        output = d / time_taken
        return output

    k = horses[n - 1][0]
    s = horses[n - 1][1]

    total_time_taken = float(d - k) / s
    for i in xrange(0, n - 1):
        k = horses[i][0]
        s = horses[i][1]
        time_taken_by_self = float(d - k) / s
        total_time_taken = max(time_taken_by_self, total_time_taken)

    output = d / total_time_taken
    return output


t = int(raw_input())
for i in xrange(1, t + 1):
    d_and_n = raw_input()
    d = int(d_and_n.split(" ")[0])
    n = int(d_and_n.split(" ")[1])

    output = calculate_speed(d, n)
    print "Case #%d: %s" % (i, output)


