import string, sys

def build_cipher():
    crypto = file('sample.in', 'r').read()
    plain = file('sample.out', 'r').read()
    assert len(crypto) == len(plain)
    cipher = {'y':'a', 'e':'o', 'q':'z'}
    for i in xrange(len(crypto)):
        fro = crypto[i]
        to = plain[i]
        if fro.isalpha():
            if fro in cipher:
                assert cipher[fro] == to
            cipher[fro] = to
        else:
            assert fro == to

    if len(cipher) == 25:
        fro = [ch for ch in string.ascii_lowercase if ch not in cipher.keys()]
        to = [ch for ch in string.ascii_lowercase if ch not in cipher.values()]
        cipher[fro[0]] = to[0]

    assert len(cipher.keys()) == 26
    assert len(set(cipher.values())) == 26
    return cipher

cipher = build_cipher()
trans = string.maketrans(str(cipher.keys()), str(cipher.values()))

N = int(sys.stdin.readline())
for i, line in enumerate(sys.stdin):
    sys.stdout.write('Case #%d: %s' % (i+1, line.translate(trans)))
