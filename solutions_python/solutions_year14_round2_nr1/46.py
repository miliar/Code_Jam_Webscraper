import fileinput

def get_canonical(s):
    i = 1
    while i < len(s):
        if s[i-1] == s[i]:
            s = s[:i-1] + s[i:]
            # del s[i]
        else:
            i += 1

    return s

def get_count_tuple(s, canonical):
    counts = []

    i = 0
    for letter in canonical:
        count = 0
        while i < len(s) and s[i] == letter:
            # if char == lette?r:
            count += 1
            i += 1

        if count == 0:
            return None

        counts.append(count)

    if i != len(s):
        return None

    return tuple(counts)

def edits(arr, target):
    cost = 0
    for a in arr:
        cost += abs(target - a)

    return cost


def distance(count_tuples):
    cost = 0
    for i in range(len(count_tuples[0])):
        lens = [t[i] for t in count_tuples]

        min_c = max(lens) * len(count_tuples)
        for target in range(min(lens), max(lens) + 1):
            min_c = min(min_c, edits(lens, target))

        cost += min_c

    return cost

inp = fileinput.input()

T = int(inp.readline())

for t in range(1,T+1):
    N = int(inp.readline())
    strings = list(inp.readline().strip() for _ in range(N))

    canonical = get_canonical(strings[0])

    fail = False
    counts = []
    for s in strings:
        count = get_count_tuple(s, canonical)

        if count is None:
            fail = True
            break

        assert sum(count) == len(s)

        counts.append(count)

    if fail:
        print("Case #{}: Fegla Won".format(t))
    else:
        print("Case #{}: {}".format(t, distance(counts)))
