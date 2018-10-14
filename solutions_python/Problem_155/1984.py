from sys import stdin

data = map(lambda x: x.split()[1], stdin.readlines()[1:])
for i, case in enumerate(data):
    res, standing = 0, 0
    for j, cnt in enumerate(case):
        if standing < j:
            res += 1
            standing += 1
        standing += int(cnt)
    print('Case #{}: {}'.format(i+1, res))
