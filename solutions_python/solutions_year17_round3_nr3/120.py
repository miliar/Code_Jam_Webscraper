from math import pi

def result(n, k, u, ps):
    ps = sorted(ps) + [1]
    print(ps)
    i = 0
    while i < len(ps) - 1:
        if u < (ps[i + 1] - ps[i]) * (i+1):
            s = (ps[i] + u / (i+1)) ** (i+1)
            for j in range(i+1, len(ps)):
                s *= ps[j]
            return s
        else:
            u -=  (ps[i + 1] - ps[i]) * (i+1)
            i += 1
    return 1

if __name__ == "__main__":
    FILE_NAME = 'C-small-1-attempt0'
    with open(FILE_NAME + '.in') as f:
        with open(FILE_NAME + '.out', 'w') as w:
            r = f.readlines()
            case = 1
            i = 1
            while i < len(r):
                buf = []
                n, k = map(int, r[i].split())
                u = float(r[i+1])
                ps = map(float, r[i+2].split())
                answer = 'Case #%d: %s\n' % (case, result(n, k, u, ps))
                print(answer)
                w.write(answer)
                case += 1
                i += 3