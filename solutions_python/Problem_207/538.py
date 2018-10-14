
c = 'ROYGBV'

def solve(va):
    n = va[0]
    va = va[1:]
    s = sorted([(v1, c[j], j) for j,v1 in enumerate(va)])
    ret = s[-1][1]
    va[s[-1][2]] -= 1
    k = 0

    while not all(v == 0 for v in va):
        s = sorted([(v1, c[j], j) for j,v1 in enumerate(va)])
        if ret[k] != s[-1][1]:
            ret += s[-1][1]
            va[s[-1][2]] -= 1
        elif s[-2][0] > 0:
            ret += s[-2][1]
            va[s[-2][2]] -= 1
        else:
            return 'IMPOSSIBLE'
        k+=1
    if ret[0] == ret[-1]:
        if len(ret) > 3 and ret[-1] != ret[-3]:
            temp = ret[-1] + ret[-2]
            ret = ret[:-2] + temp
            return ret
        return 'IMPOSSIBLE'
    return ret
            

f = open('a.in')

cases = int(f.readline())
for i in range(1, cases + 1):
    v = [int(v) for v in f.readline().split()]
    print('Case #%s: '%i + solve(v))
