import fileinput
import sys
from collections import namedtuple


def read_input():
    # gets next line from the file specified as argument or stdin
    # useful to debug within PyCharm, because you can't redirect stdin :-(
    # first time, initialize a function attribute (it's like a static local function in C++)
    # that will keep state across invocations
    if not hasattr(read_input, 'input'):
        read_input.input = fileinput.input()
    return read_input.input.next().strip()


# Horse = namedtuple('Horse','K S')

def time_to_arrive(D, horse):
    dist = D - horse[0]
    time = dist / float(horse[1])
    return time


def solve(D, horses):
    times_to_arrive = [time_to_arrive(D, horse) for horse in horses]
    slowest_time = max(times_to_arrive)
    my_speed = D / slowest_time
    return my_speed


if __name__ == "__main__":
    T = int(read_input())
    for i in xrange(1, T + 1):
        D, N = [int(s) for s in read_input().split(' ')]
        horses = []
        for j in range(0,N):
            horses.append(tuple([int(s) for s in read_input().split(' ')]))
        solution = solve(D, horses)
        print("Case #%d: %f" % (i, solution))
        sys.stderr.write('%d\n' % (i,))
