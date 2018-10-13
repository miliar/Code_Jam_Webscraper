from sys import stdin

eng_list = ['a zoo',
            'our language is impossible to understand',
            'there are twenty six factorial possibilities',
            'so it is okay if you want to just give up']
glr_list = ['y qee',
            'ejp mysljylc kd kxveddknmc re jsicpdrysi',
            'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
            'de kr kd eoya kw aej tysr re ujdr lkgc jv']

tbl = {' ': ' '}


def solve():
    T = int(stdin.readline())
    for X in range(T):
        encoded = stdin.readline().strip()
        decoded = ''.join([tbl[x] for x in encoded])
        print 'Case #%d: %s' % (X + 1, decoded)


def prepare_table():
    unmapped = [x for x in range_az()]
    for ch in range_az(): tbl[ch] = None
    
    for i in range(len(eng_list)):
        for j in range(len(eng_list[i])):
            if eng_list[i][j] in unmapped:
                tbl[glr_list[i][j]] = eng_list[i][j]
                unmapped.remove(eng_list[i][j])

    # now we have only one pair of letters left unmapped (z -> q)
    for ch in range_az():
        if tbl[ch] is None:
            tbl[ch] = unmapped[0]
            break
        

def range_az():
    return [chr(x) for x in range(ord('a'), ord('z') + 1)]


if __name__ == '__main__':
    prepare_table()
    solve()
