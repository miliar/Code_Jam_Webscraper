import sys


def main(in_stream, out_stream):
    t = int(in_stream.readline())
    for tc in range(t):
        c, f, x = map(lambda x: float(x), in_stream.readline().split())
        t = x / 2
        fc = 0
        ft = 0
        while True:
            ft += c / (2 + fc * f)
            fc += 1
            tt = ft + x / (2 + fc * f)
            if t < tt:
                break
            t = tt
        out_stream.write("Case #%d: %.7f\n" % (tc + 1, t))

if __name__ == '__main__':
    # main(sys.stdin, sys.stdout)
    main(open('B-large.in', 'r'), open('B-large-out.txt', 'w'))