def binary_v(d):
    x = []
    while d > 0:
        x.append(d%2)
        d = d/2
    return x

def transform_str(st, idx, k):
    cha = []
    for i in range(len(st)):
        if idx <= i < (idx + k):
            cha.append('+' if st[i] == '-' else '-')
        else:
            cha.append(st[i])
    return ''.join(cha)

def apply_operation(xst, bvalue, k):
    v = ''.join(['+'] * len(xst))
    for j in range(len(bvalue)):
        if bvalue[j] == 1:
            xst = transform_str(xst, j, k)
    if v == xst:
        return sum(bvalue)
    return -1

#print apply_operation('---+-++-', [1, 0, 0, 0, 1, 1, 0, 0], 3)

def min_cake(st, k):
    v = ''.join(['+'] * len(st))
    if v == st:
        return 0
    ans = 0
    while v != st:
        idx = st.find('-')
        if idx < len(st) - k + 1:
            st = transform_str(st, idx, k)
            ans = ans + 1
        else:
            return 'IMPOSSIBLE'

    return ans


with open('/Users/girishkadli/Desktop/codejam/test.txt', 'r') as f:
    lines = f.readlines()
    t = int(lines[0])
    for i in range(1, t + 1):
        st = lines[i].split(' ')
        cake = st[0]
        k = int(st[1])
        print 'Case #%s: %s' % (str(i), str(min_cake(cake, k)))


