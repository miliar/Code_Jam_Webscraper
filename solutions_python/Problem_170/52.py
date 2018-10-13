from copy import deepcopy

def solve():
    n = int(raw_input())
    eng = set(raw_input().split())
    fr = set(raw_input().split())
    a = []

    has = eng.intersection(fr)

    for i in range(n - 2):
        a.append(set(raw_input().split()))
        a[-1].difference_update(has)

    eng = eng.difference(has)
    fr = fr.difference(has)

    ans = 10 ** 9
    for i in range(1 << (n - 2)):
        ew = set()
        fw = set()

        for j in range(n - 2):
            if (1 << j) & i:
                ew.update(a[j])
            else:
                fw.update(a[j])
        ew.update(eng)
        fw.update(fr)
        ans = min(ans, len(ew.intersection(fw)))
    return ans + len(has)

for _ in range(int(raw_input())):
    answer = solve()
    print('Case #%d: %d' % (_ + 1, answer))

