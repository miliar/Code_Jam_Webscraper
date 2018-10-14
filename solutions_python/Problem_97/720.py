'''
4
1 9
10 40
100 500
1111 2222
'''

f = open('C-large.in')

test_count = int(f.readline())

lines = f.readlines()
split_lines = (line.strip().split(' ') for line in lines)
inputs = [(int(chunks[0]), int(chunks[1])) for chunks in split_lines if len(chunks) == 2]

# Make sure we have the right number of input pairs.
assert test_count == len(lines)

def recycle_count(a,b):
    sA = str(a)
    sB = str(b)
    assert len(sA) == len(sB)
    length = len(sA)

    if length <= 1:
        return 0

    c = 0

    for n in range(a, b):
        sN = str(n)

        # 'n' must have no leading zeroes.
        if sN[0] == '0':
            assert False

        rearranged = [sN[i:] + sN[:i] for i in range(1,length)]


        #print(s)
        '''for x in (m for m in rearranged if sA <= sN < m <= sB):
            print('({0}, {1})'.format(n, x))'''

        c += sum(1 for m in set(rearranged) if sA <= sN < m <= sB)

    return c


out_file = open('C-large.out', 'w')

for i, (a,b) in enumerate(inputs, 1):
    c = recycle_count(a,b)
    print('Case #{0}: {1}'.format(i, c))
    out_file.write('Case #{0}: {1}\n'.format(i, c))

out_file.close()