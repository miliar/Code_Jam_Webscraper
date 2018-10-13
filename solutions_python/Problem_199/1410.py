
tests = []
with open('input.in', 'r') as f:
    T = int(f.readline())
    for i in range(T):
        tests.append(f.readline().strip().split(' '))

with open('ouput.out', 'w') as f:
    case = 1
    for pans, size_str in tests:
        size = int(size_str)
        pans_l = [1 if p == '+' else 0 for p in list(pans)]

        i = 0
        changes = 0
        while i < len(pans_l):
            if pans_l[i] == 0 and i + size <= len(pans_l):
                changes += 1
                for j in range(i, i + size):
                    pans_l[j] = 1 - pans_l[j]
            i += 1

        if 0 in pans_l:
            f.write("Case #%d: IMPOSSIBLE\n" % case)
        else:
            f.write("Case #%d: %d\n" % (case, changes))
        case += 1

