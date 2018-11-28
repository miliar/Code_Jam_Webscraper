import sys


def main(in_stream, out_stream):
    t = int(in_stream.readline())
    for tc in range(t):
        a1 = int(in_stream.readline())
        r1 = [in_stream.readline() for _ in range(4)]
        a2 = int(in_stream.readline())
        r2 = [in_stream.readline() for _ in range(4)]
        a = set(map(lambda x: int(x), r1[a1 - 1].split())) & set(map(lambda x: int(x), r2[a2 - 1].split()))
        out_stream.write("Case #%d: " % (tc + 1))
        if len(a) > 1:
            out_stream.write("Bad magician!\n")
        elif len(a):
            out_stream.write("%d\n" % list(a)[0])
        else:
            out_stream.write("Volunteer cheated!\n")

if __name__ == '__main__':
    # main(sys.stdin, sys.stdout)
    main(open('A-small-attempt.in', 'r'), open('A-small-out.txt', 'w'))