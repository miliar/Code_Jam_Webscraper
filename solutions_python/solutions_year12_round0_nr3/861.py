"""
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

"""
import sys

def rotate(i, j):
    k = i[j:] + i[:j]
    k = str(int(k))
    if int(i) < int(k):
        return (i, k)
    return (k, i)

def solve(A, B):
    d = {}
    count = 0
    AA = int(A)
    BB = int(B)

    for i in range(AA, BB + 1):
        for j in range(len(A) - 1):
            (l, m) = rotate(str(i), j + 1)
            ll = int(l)
            mm = int(m)
            if (ll, mm) not in d:
                if len(l) == len(m) and ll >= AA and ll < mm and mm <= BB:
                    d[(ll,mm)] = ''
                    count = count + 1

    return count

input_file_name = sys.argv[1]
output_file_name = sys.argv[2]

input_file = open(input_file_name, 'r')
output_file = open(output_file_name, 'w')

input_file_lines = input_file.readlines()

case = 1

for line in input_file_lines[1:]:
    l = line.split()
    output_file.write('Case #' + str(case) + ': ' + str(solve(l[0], l[1])) + '\n')
    case = case + 1
"""
-----BEGIN PGP SIGNATURE-----
Version: GnuPG/MacGPG2 v2.0.17 (Darwin)
Comment: GPGTools - http://gpgtools.org

iF4EAREIAAYFAk+I6/wACgkQf7sAhIwsAlA5QAEAjYoxezCKfRGQaegm5oit4ixZ
ZNKhXi4ME8mCDwcEWFIA/REOw8uCkpACVOn8In9axstqHTw/D5vhMkr58QEVb4j1
=XL8P
-----END PGP SIGNATURE-----
"""
