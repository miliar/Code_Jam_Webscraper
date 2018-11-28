from sys import stdin

data = stdin.readlines()

for i, case in enumerate(data[1:], 1):
    pan, k = case.split()
    k = int(k)
    pan = list(map(lambda x: (ord(x)-ord('+'))//2, pan))
    s = len(pan)
    sub = [0]*s
    acc = 0
    res = 0
    for j in range(s-k):
        acc -= sub[j]
        if (pan[j] + acc)%2:
            res += 1
            acc += 1
            sub[j+k] += 1
    for j in range(s-k, s):
        acc -= sub[j]
        pan[j] = (pan[j] + acc)%2
    if pan[-k:] == [1]*k:
        res += 1
    elif pan[-k:] != [0]*k:
        res = 'IMPOSSIBLE'
    print('Case #{}: {}'.format(i, res))
