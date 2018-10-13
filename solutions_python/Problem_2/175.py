
import sys

def line():
    return sys.stdin.readline().rstrip("\r\n")

def minutes(s):
    hours, minutes = map(int, s.split(":"))
    return hours*60 + minutes


oposite = dict(zip("ab", "ba"))
def testcase():
    T = int(line())
    NA, NB = (int(x) for x in line().strip().split())
    def read_timetable(station, n):
        for i in xrange(n):
            start, end = map(minutes, line().strip().split())
            yield (start, station, +1)
            yield (end+T, oposite[station], -1)
    timetable = sorted(
                list(read_timetable("a", NA)) +
                list(read_timetable("b", NB))
                )
    count = dict(a=0, b=0)
    ex = dict(a=0, b=0)
    for t, station, delta in timetable:
        count[station] += delta
        ex[station] = max(ex[station], count[station])
    return (ex["a"], ex["b"])

def main():
    n_cases = int(line())
    for t_case in xrange(1, n_cases+1):
        a, b = testcase()
        print "Case #%d: %d %d" % (t_case, a, b)

if __name__ == "__main__":
    main()

# vim: ts=4 sw=4 et
