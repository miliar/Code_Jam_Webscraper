def clear_out(ds, affected):
    for i in xrange(affected, len(ds)):
        ds[i] = 9

def remove_zeros(ds):
    index = 0
    while ds[index] == 0:
        index += 1
    return ds[index:]

def fix_before(ds, index):
    value = ds[index]
    first_index = ds.index(value)
    ds[first_index] -= 1
    for i in xrange(first_index + 1, index + 1):
        ds[i] = 9

def solve(ds):
    length = len(ds)
    max_value = ds[0]
    for index in xrange(length):
        if index == length - 1:
            continue
        if ds[index] > ds[index + 1]:
            fix_before(ds, index)
            clear_out(ds, index+1)
    ds = remove_zeros(ds)
    s = map(str, ds)
    return ''.join(s)

t = int(raw_input())
for case in xrange(1, t+1):
    n = raw_input()
    digits = []
    for digit in n:
        digits.append(int(digit))
    num = solve(digits)
    print 'Case #{}: {}'.format(case, num)

