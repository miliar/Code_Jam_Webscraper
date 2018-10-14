def main(in_stream, out_stream):
    t = int(in_stream.readline())
    for tc in range(t):
        n, m = map(lambda x: int(x), in_stream.readline().split())
        l = []
        for i in range(n):
            l.append([])
            line = in_stream.readline().split()
            for j in range(m):
                l[-1].append(int(line[j]))
        out_stream.write("Case #%d: %s\n" % (tc + 1, "YES" if check(l) else "NO"))

def check(l):
    n = len(l)
    m = len(l[0])
    for i in range(n):
        for j in range(m):
            yes = True
            for k in range(n):
                if l[i][j] < l[k][j]:
                    yes = False
                    break
            if not yes:
                yes = True
                for k in range(m):
                    if l[i][j] < l[i][k]:
                        yes = False
                        break
                if not yes:
                    return False
    return True

if __name__ == '__main__':
#    import sys
#    main(sys.stdin, sys.stdout)
    main(open("B-large.in", "r"), open("b-large.out.txt", "w"))
