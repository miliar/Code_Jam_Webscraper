import sys
import itertools

def main(in_stream, out_stream):
    t = int(in_stream.readline())
    for tc in range(t):
        X, Y = map(lambda x: int(x), in_stream.readline().split())
        out_stream.write("Case #%d: %s\n" % (tc + 1, ("WE" * X if X > 0 else "EW" * (-X)) + ("SN" * Y if Y > 0 else "NS" * (-Y))))

if __name__ == '__main__':
#    main(sys.stdin, sys.stdout)
    main(open("B-small-attempt0.in", "r"), open("b-small-out.txt", "w"))