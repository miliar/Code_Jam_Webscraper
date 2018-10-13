"""
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

"""
import sys

def ii(i):
    r = []
    for c in i:
        r.append(int(c))
    return r

def solve(N, S, p, t):
    t = ii(t)
    n = 0

    for i in t:
        m = i % 3
        j = i / 3
        if m == 0:
            if j >= p:
                n = n + 1
            elif j + 1 >= p and S > 0 and j + 1 <= 10 and j - 1 >= 0:
                S = S - 1
                n = n + 1
        elif m == 2:
            if j + 1 >= p:
                n = n + 1
            elif j + 2 >= p and S > 0 and j + 2 <= 10:
                n = n + 1
                S = S - 1
        else:
            if j + 1 >= p:
                n = n + 1

    return n

input_file_name = sys.argv[1]
output_file_name = sys.argv[2]

input_file = open(input_file_name, 'r')
output_file = open(output_file_name, 'w')

input_file_lines = input_file.readlines()

case = 1

for line in input_file_lines[1:]:
    l = line.split()
    output_file.write('Case #' + str(case) + ': ' + str(solve(int(l[0]), int(l[1]), int(l[2]), l[3:])) + '\n')
    case = case + 1
"""
-----BEGIN PGP SIGNATURE-----
Version: GnuPG/MacGPG2 v2.0.17 (Darwin)
Comment: GPGTools - http://gpgtools.org

iF4EAREIAAYFAk+I31sACgkQf7sAhIwsAlAQ6QEAighGU5orkCVdQJbYHfBRSpA8
NwwyBaDo235/P7deoBQA/2w63FZaCoFe8Z7hKD8MIN1gjkXxsTSa0Cq21J0rXtTJ
=LdDz
-----END PGP SIGNATURE-----
"""
