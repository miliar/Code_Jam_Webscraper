import sys

input = sys.stdin

test = int(input.readline())

for test_num in range(1, test+1):
    l, count = map(int, input.readline().split(' '))
    s = input.readline().rstrip() * count

    mult_dict = {
        ('1', '1'): '1',
        ('1', 'i'): 'i',
        ('1', 'j'): 'j',
        ('1', 'k'): 'k',
        ('i', '1'): 'i',
        ('i', 'i'): '-1',
        ('i', 'j'): 'k',
        ('i', 'k'): '-j',
        ('j', '1'): 'j',
        ('j', 'i'): '-k',
        ('j', 'j'): '-1',
        ('j', 'k'): 'i',
        ('k', '1'): 'k',
        ('k', 'i'): 'j',
        ('k', 'j'): '-i',
        ('k', 'k'): '-1'
    }

    def mult(a, b):
        res = mult_dict[a[-1], b[-1]]
        if ('-' in a) != ('-' in b):
            res = '-' + res
        if '--' in res:
            res = res[2:]
        return res

    starts_of_k = set()
    cur = '1'
    for i, c in enumerate(s[::-1]):
        cur = mult(c, cur)
        if cur == 'k':
            starts_of_k.add(len(s) - i - 1)

    cur = '1'
    i_was = False
    res = 'NO'
    for i, c in enumerate(s):
        cur = mult(cur, c)
        if cur == 'i':
            i_was = True
        elif cur == 'k' and i_was:
            if (i + 1) in starts_of_k:
                res = 'YES'
                break

    print('Case #{}: {}'.format(test_num, res))
