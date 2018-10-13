import sys

dec = dict(zip('0123456789', '9012345678'))
cat = ''.join

def solve(ds):
    try:
        i = next(i for i, c in enumerate(ds)
                 if c > ds[i+1])
        ds[i+1:] = ['9'] * (len(ds) - i - 1)
        while True:
            ds[i] = dec[ds[i]]
            if i != 0 and ds[i-1] > ds[i]:
                ds[i] = '9'
                i -= 1
            else:
                break
        if ds[0] == '0':
            ds.pop(0)
    except (StopIteration, IndexError):
        pass
    return ds

for t, n in enumerate(sys.stdin.read().split()[1:], 1):
    print('Case #{}: {}'.format(t, cat(solve(list(n)))))
