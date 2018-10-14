"""
Code Jam 2011
Qualify A
"""
import sys

def min_time(directive):
    bot = { 'O': (0, 1), # (time, position)
            'B': (0, 1) }
    time = 0
    for d_bot, d_loc in directive:
        distance = abs(bot[d_bot][1] - d_loc)
        time = max(time, bot[d_bot][0] + distance) + 1
        bot[d_bot] = (time, d_loc)
    return time

def main():
    num_tests = int(sys.stdin.readline())
    for t in range(1, num_tests + 1):
        line = sys.stdin.readline().split()
        line.pop(0) # ignore number of steps, infered from directive below
        directive = zip(line[::2], [int(x) for x in line[1::2]])
        mtime = min_time(directive)
        print "Case #%d: %d" % (t, mtime)

if __name__ == '__main__':
    main()
