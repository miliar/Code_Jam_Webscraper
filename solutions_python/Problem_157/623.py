def isRight(s):
    d = {
        '11' : '1', '1!' : '!', '!1' : '!', '!!' : '1',
        '1i' : 'i', '1I' : 'I', '!i' : 'I', '!I' : 'i',
        '1j' : 'j', '1J' : 'J', '!j' : 'J', '!J' : 'j',
        '1k' : 'k', '1K' : 'K', '!k' : 'K', '!K' : 'k',
        'i1' : 'i', 'i!' : 'I', 'I1' : 'I', 'I!' : 'i',
        'ii' : '!', 'iI' : '1', 'Ii' : '1', 'II' : '!',
        'ij' : 'k', 'iJ' : 'K', 'Ij' : 'K', 'IJ' : 'k',
        'ik' : 'J', 'iK' : 'j', 'Ik' : 'j', 'IK' : 'J',
        'j1' : 'j', 'j!' : 'J', 'J1' : 'J', 'J!' : 'j',
        'ji' : 'K', 'jI' : 'k', 'Ji' : 'k', 'JI' : 'K',
        'jj' : '!', 'jJ' : '1', 'Jj' : '1', 'JJ' : '!',
        'jk' : 'i', 'jK' : 'I', 'Jk' : 'I', 'JK' : 'i',
        'k1' : 'k', 'k!' : 'K', 'K1' : 'K', 'K!' : 'k',
        'ki' : 'j', 'kI' : 'J', 'Ki' : 'J', 'KI' : 'j',
        'kj' : 'I', 'kJ' : 'i', 'Kj' : 'i', 'KJ' : 'I',
        'kk' : '!', 'kK' : '1', 'Kk' : '1', 'KK' : '!',
    }

    i = '1'
    for c in s:
        i = d[i+c]
    if i != '!':
        return "NO"

    i = '1'
    for ii, ci in enumerate(s[:-2]):
        i = d[i+ci]
        if i == 'i':
            j = '1'
            for ij, cj in enumerate(s[ii+1:-1]):
                j = d[j+cj]
                if j == 'j':
                    k = '1'
                    for ck in s[ii+ij+2:]:
                        k = d[k+ck]
                    if k == 'k':
                        return "YES"
    return "NO"

def test():
    assert isRight('ik') == 'NO'
    assert isRight('ikik') == 'YES'
    assert isRight('ijkijkijk') == 'YES'
    assert isRight('kjikjikji') == 'NO'
    assert isRight('jijijijijiji') == 'YES'
    assert isRight(1000*'i') == 'NO'

if __name__ == '__main__':
    test()
    import sys
    with sys.stdin as f:
        T = int(f.readline())
        k = 1
        for j in range(T):
            L, X = [int(i) for i in f.readline().split()]
            print "Case #%d: %s" % (k, isRight(X*f.readline().strip()))
            k += 1
