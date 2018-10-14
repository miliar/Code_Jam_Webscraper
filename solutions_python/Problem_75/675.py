import sys
from collections import deque

def readline():
    return sys.stdin.readline().strip()

def solve(line):
    #print line
    l = deque(line.split())
    pairs = {}
    opposed = {}

    pc = int(l.popleft())
    for i in range(pc):
        v = l.popleft()
        pairs[tuple(v[:2])] = v[2]
        pairs[tuple(reversed(v[:2]))] = v[2]

    oc = int(l.popleft())
    for i in range(oc):
        v = l.popleft()
        if v[0] not in opposed:
            opposed[v[0]] = set()
        if v[1] not in opposed:
            opposed[v[1]] = set()
        opposed[v[0]].add(v[1])
        opposed[v[1]].add(v[0])

    chars = int(l.popleft())
    seq = l.popleft()
    #print pc, oc, seq, pairs, opposed

    def opposes(r, char):
        if char not in opposed:
            return False
        z = opposed[char]
        for val in r:
            if val in z:
                return True
        return False

    ret = []
    for i in seq:
        if len(ret) > 0 and (ret[-1], i) in pairs:
            ret[-1] = pairs[(ret[-1], i)]
        elif opposes(ret, i):
            ret = []
        else:
            ret.append(i)
    return "[" + ", ".join(ret) + "]"

def main():
    n_inputs = int(readline())
    for i in range(n_inputs):
        print "Case #%d: %s" % (i + 1, solve(readline()))

if __name__ == "__main__":
    main()
