from bisect import insort

def solution(inputs):
    n, k = inputs.split()
    n, k = int(n), int(k)
    l, r = None, None
    emptyrun_counts = {i: 0 for i in range(1, n)}
    emptyrun_counts[n] = 1
    existing = [n]

    while k:
        if emptyrun_counts[existing[-1]] >= k:
            if existing[-1] % 2:
                return ((existing[-1] - 1) // 2, (existing[-1] - 1) // 2)
            else:
                return (existing[-1] // 2, (existing[-1] // 2) - 1)
        else:
            if existing[-1] % 2:
                l, r = (existing[-1] - 1) // 2, (existing[-1] - 1) // 2
            else:
                l, r = (existing[-1] // 2) - 1, existing[-1] // 2
            k -= emptyrun_counts[existing[-1]]

            if l:
                emptyrun_counts[l] += emptyrun_counts[existing[-1]]
            if r:
                emptyrun_counts[r] += emptyrun_counts[existing[-1]]
            emptyrun_counts[existing[-1]] = 0
            existing = existing[:-1]
            if l not in existing:
                insort(existing, l)
            if r not in existing:
                insort(existing, r)



filename = input()
f = open(filename + ".in")
o = open(filename + ".out", "w")

t = int(f.readline())
for case in range(t):
    o.write("Case #{}: {} {}\n".format(case + 1, *solution(f.readline().strip())))

f.close()
o.close()