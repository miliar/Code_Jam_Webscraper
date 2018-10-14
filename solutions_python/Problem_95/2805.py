#!/usr/bin/env python3
# Problem A. Speaking in Tongues

from string import ascii_lowercase

# Generate the cipher based on examples
rev_cipher = {'y': 'a', 'e': 'o', 'q': 'z'}
ciphertext = 'ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv'
plaintext = 'ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup'

for i in range(len(ciphertext)):
    rev_cipher[ciphertext[i]] = plaintext[i]
cipher = {v: k for k, v in rev_cipher.items()}
for letter in ascii_lowercase:
    if letter not in rev_cipher:
        for unused in ascii_lowercase:
            if unused not in cipher:
                rev_cipher[letter] = unused
                cipher[unused] = letter

f = open('input.txt', 'r')
n = int(f.readline())

for i in range(1, n+1):
    print('Case #%d: ' % (i), end='')
    ciphertext = f.readline().strip()
    for letter in ciphertext:
        if letter == ' ': print(' ', end='')
        else:
            print(rev_cipher[letter], end='')
    print()

