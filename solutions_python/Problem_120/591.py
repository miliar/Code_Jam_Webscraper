import sys
import math

def main(in_stream, out_stream):
    t = int(in_stream.readline())
    for tc in range(t):
        r, t = map(lambda x: int(x), in_stream.readline().split())
        a = 2
        b = 2 * r - 1
        c = -t
        x = math.floor((-b + math.sqrt(b ** 2 - 4 * a * c)) / float(2 * a))
        while a * x ** 2 + b * x > t:
            x -= 1
        out_stream.write("Case #%d: %d\n" % (tc + 1, x))

if __name__ == '__main__':
#    main(sys.stdin, sys.stdout)
    main(open("A-small-attempt0.in", "r"), open("A-small-out.txt", "w"))
