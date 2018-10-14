"""
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

"""
import sys

key = {'a':'y', 'b':'h', 'c':'e', 'd':'s', 'e':'o', 'f':'c', 'g':'v', 'h':'x', 'i':'d', 'j':'u', 'k':'i', 'l':'g', 'm':'l', 'n':'b', 'o':'k', 'p':'r', 'q':'z', 'r':'t', 's':'n', 't':'w', 'u':'j', 'v':'p', 'w':'f', 'x':'m', 'y':'a', 'z':'q'}

def decrypt(s):
    ret = ''
    for c in s:
        if c in key:
            ret = ret + key[c]
        else:
            ret = ret + c
    return ret

input_file_name = sys.argv[1]
output_file_name = sys.argv[2]

input_file = open(input_file_name, 'r')
output_file = open(output_file_name, 'w')

input_file_lines = input_file.readlines()

case = 1

for line in input_file_lines[1:]:
    l = line.rstrip()
    output_file.write('Case #' + str(case) + ': ' + decrypt(l) + '\n')
    case = case + 1
"""
-----BEGIN PGP SIGNATURE-----
Version: GnuPG/MacGPG2 v2.0.17 (Darwin)
Comment: GPGTools - http://gpgtools.org

iF4EAREIAAYFAk+Iv+kACgkQf7sAhIwsAlBFowD/XmwC8HIgd+D96buUHaYUbhcd
CToP9Q7c3uLJsulYQlwA/iaHCS7oSAdZKmEKQR2e5iR/61546wVmf/C0jHW1Efhn
=kAKv
-----END PGP SIGNATURE-----
"""
