import sys
import math
import copy

def main(in_stream, out_stream):
    t = int(in_stream.readline())
    for tc in range(t):
        e, r, n = map(lambda x: int(x), in_stream.readline().split())
        v = list(map(lambda x: int(x), in_stream.readline().split()))
        mx = {e: 0}
        for i in range(n):
            nmx = copy.deepcopy(mx)
            for j in sorted(mx.keys(), reverse=True):
                for k in range(j, 0, -1):
                    if min((k + r, e)) not in nmx or nmx[min((k + r, e))] < mx[j] + (j - k) * v[i]:
                        nmx[min((k + r, e))] = mx[j] + (j - k) * v[i]
                if min((r, e)) not in nmx or nmx[min((r, e))] < mx[j] + j * v[i]:
                    nmx[min((r, e))] = mx[j] + j * v[i]
            mx = nmx
        out_stream.write("Case #%d: %d\n" % (tc + 1, max(mx.values())))

if __name__ == '__main__':
#    main(sys.stdin, sys.stdout)
    main(open("B-small-attempt1.in", "r"), open("B-small-out.txt", "w"))
