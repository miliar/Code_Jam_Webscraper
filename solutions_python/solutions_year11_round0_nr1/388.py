import sys

n = int(sys.stdin.readline())

for case in range(n):
    prog = sys.stdin.readline()
    prog = filter(lambda x: len(x) > 0,
                  map(lambda x: x.strip(), prog.split(" ")))
    Blast, Btime = 1, 0
    Olast, Otime = 1, 0
    for i in range(1, int(prog[0])+1):
        pos = int(prog[2*i])
        if prog[2*i-1] == 'O':
            Otime = max(Btime, Otime + abs(Olast - pos)) + 1
            Olast = pos
        elif prog[2*i-1] == 'B':
            Btime = max(Otime, Btime + abs(Blast - pos)) + 1
            Blast = pos
        else:
            exit(1)
    print 'Case #%d:' % (case + 1), max(Btime, Otime)