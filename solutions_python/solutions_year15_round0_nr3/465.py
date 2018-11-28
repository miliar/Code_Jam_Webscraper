def mul_quartenions(a, b):
    mul_table = {
        ('i', 'i'): ('1', -1),
        ('i', 'j'): ('k', 1),
        ('i', 'k'): ('j', -1),
        ('j', 'i'): ('k', -1),
        ('j', 'j'): ('1', -1),
        ('j', 'k'): ('i', 1),
        ('k', 'i'): ('j', 1),
        ('k', 'j'): ('i', -1),
        ('k', 'k'):  ('1', -1),
    }
    if a[0] == '1':
        return (b[0], b[1]*a[1])
    if b[0] == '1':
        return (a[0], b[1]*a[1])
    else:
        t = mul_table[(a[0], b[0])]
        return (t[0], t[1]*a[1]*b[1])

def quartenify(string, n):
    if n > 20:
        n = (n % 4) + 20
    return [(s, 1) for s in string]*n


def find_ijk(q):
    if len(q) == 1 or reduce(mul_quartenions, q) != ('1', -1):
        return 'NO'

    current_first = q[0]
    for i in range(1, len(q)):
        if current_first == ('i', 1):
            break
        current_first = mul_quartenions(current_first, q[i])

    current_second = q[i]
    for j in xrange(i + 1, len(q)):
        if current_second == ('j', 1) and reduce(mul_quartenions, q[j:]) == ('k', 1):
            return 'YES'
        current_second = mul_quartenions(current_second, q[j])
    return 'NO'

T = int(raw_input())

for i in range(T):
    L, X = map(int, raw_input().split(" "))
    string = raw_input()
    print "Case #%i: %s" % (i+1, find_ijk(quartenify(string, X)))
