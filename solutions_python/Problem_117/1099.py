import fileinput

f = fileinput.input()
# f = fileinput.input('B-small-attempt0.in')
# f = fileinput.input('sample.in')

T = int(f.readline())


def check(a):
    er = len(a)-1
    ec = len(a[0])-1
    t = list(map(list, zip(*a))) # transposed
    for r in range(len(a)):
        for c in range(len(a[0])):
            # if a[r][c] < min(max(a[r][0], a[r][ec]), max(a[0][c], a[er][c])): return False
            if a[r][c] < max(a[r]) and a[r][c] < max(t[c]): return False
    return True

for t in range(1, T+1):
    ln = fileinput.lineno()-1
    N, M = map(int, f.readline().strip().split())
    a = []
    for n in range(0, N):
        a.append(list(map(int, f.readline().strip().split())))
    ok = check(a)
    print("Case #%s: %s"%(t, 'YES' if ok else 'NO'))
