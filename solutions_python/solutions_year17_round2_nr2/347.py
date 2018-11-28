import fileinput
import sys

def read_input():
    # gets next line from the file specified as argument or stdin
    # useful to debug within PyCharm, because you can't redirect stdin :-(
    # first time, initialize a function attribute (it's like a static local function in C++)
    # that will keep state across invocations
    if not hasattr(read_input, 'input'):
        read_input.input = fileinput.input()
    return read_input.input.next().strip()




def solve(N,R,O,Y,G,B,V):
    unicorns = list(reversed(sorted([[R,'R'],[O,'O'],[Y,'Y'],[G,'G'],[B,'B'],[V,'V']])))
    stables = [None] * N
    free = N

    if unicorns[0][0] > N/2:
        return 'IMPOSSIBLE'

    next = 0
    while unicorns[0][0]:
        stables[next] = unicorns[0][1]
        unicorns[0][0]-=1
        next += 2
        free -= 1

    unicorns.pop(0)

    if unicorns[0][0] < free/2:
        return 'IMPOSSIBLE'

    while unicorns:
        if next >= N:
            next = 0

        while stables[next] is not None:
            next += 1

        stables[next] = unicorns[0][1]
        unicorns[0][0] -= 1
        next += 2
        free -= 1

        while unicorns and unicorns[0][0] == 0:
            unicorns.pop(0)

    return ''.join(stables)


if __name__ == "__main__":
    T = int(read_input())
    for i in xrange(1, T+1):
        N,R,O,Y,G,B,V = [int(s) for s in read_input().split(' ')]
        solution = solve(N,R,O,Y,G,B,V)
        print("Case #%d: %s" % (i,solution))
        sys.stderr.write('%d\n' % (i,))

