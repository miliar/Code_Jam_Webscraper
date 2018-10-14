def result(d, n, buf):
    m = max((1.0*d-x[0])/x[1] for x in buf)
    print(d/m)
    return d/m 

if __name__ == "__main__":
    FILE_NAME = 'A-large'
    with open(FILE_NAME + '.in') as f:
        with open(FILE_NAME + '.out', 'w') as w:
            r = f.readlines()
            case = 1
            i = 1
            while i < len(r):
                buf = []
                d, n = map(int, r[i].split())
                for j in range(n):
                    buf.append(map(int, r[i + 1 + j].split()))
                w.write('Case #%d: %s\n' % (case, result(d, n, buf)))
                case += 1
                i += n + 1