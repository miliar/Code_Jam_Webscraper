
import sys

def count_intersects(wires):
    ret = 0
    n = len(wires)
    for i in range(n):
        cw = wires[i]
        for j in range(i + 1, n):
            nextw = wires[j]
            if cw[0] < nextw[0] and cw[1] > nextw[1]:
                ret = ret + 1
            if cw[0] > nextw[0] and cw[1] < nextw[1]:
                ret = ret + 1
    return ret
                

if __name__ == '__main__':
    stdin = sys.stdin
    num_cases = stdin.readline()

    for i in range(int(num_cases)):
        line = stdin.readline()
        N = int(line)
        
        wires = []
        for h in range(N):
            line = stdin.readline()
            w = map(int, line.split())
            wires.append(w)

        res = count_intersects(wires)

        print "Case #%d: %d" % (i+1, res)
