from math import pi

def result(n, k, buf):
    m = 0
    cache = []
    for i in range(len(buf)):
        x = buf[i]
        cand = x[0]**2 + x[0] * x[1] * 2
        news = sorted([t for t in buf[:i] + buf[i+1:] if t[0] <= x[0]], key= lambda y: -y[0]*y[1])
        for i in range(min(k - 1, len(news))):
            cand += 2 * news[i][0] * news[i][1]
        m = max(m, cand)
    print(m*pi)
    return m * pi

if __name__ == "__main__":
    FILE_NAME = 'A-large'
    with open(FILE_NAME + '.in') as f:
        with open(FILE_NAME + '.out', 'w') as w:
            r = f.readlines()
            case = 1
            i = 1
            while i < len(r):
                buf = []
                n, k = map(int, r[i].split())
                for j in range(n):
                    buf.append(map(int, r[i + 1 + j].split()))
                w.write('Case #%d: %s\n' % (case, result(n, k, buf)))
                case += 1
                i += n + 1