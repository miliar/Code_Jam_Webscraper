import sys


fp = open(sys.argv[1])
N = int(fp.readline().strip())

def foo():
    [N,R,O,Y,G,B,V] = [int(x) for x in fp.readline().strip().split(" ")]
    ma = max(R,O,Y,G,B,V)
    if (ma > N / 2):
        return "IMPOSSIBLE"
    CC = sorted([('R', R), ('Y', Y), ('B', B)], key=lambda x: -x[1])
    tokens = [[CC[0][0]] for x in range(CC[0][1])]
    pos = 0
    for i in range(CC[1][1]):
        tokens[pos % CC[0][1]].append(CC[1][0])
        pos += 1
    for i in range(CC[2][1]):
        tokens[pos % CC[0][1]].append(CC[2][0])
        pos += 1
    tokens = ''.join([''.join(x) for x in tokens])
    return tokens

for case in range(N):
    print "Case #%d: %s" % (case + 1, foo())

fp.close()
