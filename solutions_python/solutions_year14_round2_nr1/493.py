__author__ = 'PavelM'


import numpy as np

def solve():
    n = int(in_file.readline())
    strings = []
    for k in range(n):
        strings.append(in_file.readline())

    letters = []
    for s in strings:
        current_letters = []
        let = None
        for sym in s:
            if sym != let:
                if let is not None:
                    current_letters.append((let, count))
                count = 1
                let = sym
            else:
                count += 1
        letters.append(current_letters)

    lengths = {len(l) for l in letters}
    if len(lengths) > 1:
        return "Fegla Won"

    c = 0
    for i in range(len(letters[0])):
        vals = [l[i] for l in letters]
        let = {v[0] for v in vals}
        if len(let) > 1:
            return "Fegla Won"

        nums = sorted([v[1] for v in vals])
        m = np.mean(nums)
        c1, c2 = 0, 0
        m1 = int(m)
        m2 = m1 + 1
        for n in nums:
            c1 += abs(m1 - n)
            c2 += abs(m2 - n)

        c += min(c1, c2)

    return c




if __name__ == '__main__':
    name = 'A-small-attempt0'
    with open('%s.out' % name, 'w') as output:
        with open('%s.in' % name) as in_file:
            n = int(in_file.readline())
            for k in range(1, n + 1):
                output.write('Case #{0}: {1}\n'.format(k, solve()))