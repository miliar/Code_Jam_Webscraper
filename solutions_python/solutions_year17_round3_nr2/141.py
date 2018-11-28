def solution(cs, js):
    if len(cs) < len(js):
        cs, js = js, cs
    cs = sorted(cs, key = lambda x: x[0])
    js = sorted(js, key = lambda x: x[0])
    if len(cs) == 2:
        if cs[1][1] - cs[0][0] <= 720:
            if len(js) == 0 or not (cs[0][0] <= js[0][0] <= cs[1][1]):
                return 2
        if 1440+cs[0][1] - cs[1][0] <= 720:
            if len(js) == 0 or not (js[0][0] < cs[1][0] or js[0][0] > cs[0][0]):
                return 2
        return 4
    return 2

if __name__ == "__main__":
    FILE_NAME = 'B-small-attempt0'
    with open(FILE_NAME + '.in') as f:
        with open(FILE_NAME + '.out', 'w') as w:
            r = f.readlines()

            case = 1
            line = 1
            while line < len(r):
                cs, js = [], []
                c, j = map(int, r[line].split())
                for i in range(c):
                    cs.append(map(int, r[line + 1 + i].split()))
                for i in range(j):
                    js.append(map(int, r[line + 1 + i + c].split()))
                answer = 'Case #%d: %s\n' % (case, solution(cs, js))
                w.write(answer)
                print(answer)
                case += 1
                line += 1 + c + j