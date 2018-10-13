# coding: utf-8

import sys

table = {
    '11': '1',   '1i': 'i',   '1j': 'j',   '1k': 'k',   '1-1': '-1', '1-i': '-i',  '1-j': '-j',  '1-k': '-k',
    'i1': 'i',   'ii': '-1',  'ij': 'k',   'ik': '-j',  'i-1': '-i', 'i-i': '1',   'i-j': '-k',  'i-k': 'j', 
    'j1': 'j',   'ji': '-k',  'jj': '-1',  'jk': 'i',   'j-1': '-j', 'j-i': 'k',   'j-j': '1',   'j-k': '-i',  
    'k1': 'k',   'ki': 'j',   'kj': '-i',  'kk': '-1',  'k-1': '-k', 'k-i': '-j',  'k-j': 'i',   'k-k': '1', 
    '-11': '-1', '-1i': '-i', '-1j': '-j', '-1k': '-k', '-1-1': '1', '-1-i': 'i',  '-1-j': 'j',  '-1-k': 'k',
    '-i1': '-i', '-ii': '1',  '-ij': '-k', '-ik': 'j',  '-i-1': 'i', '-i-i': '-1', '-i-j': 'k',  '-i-k': '-j',
    '-j1': '-j', '-ji': 'k',  '-jj': '1',  '-jk': '-i', '-j-1': 'j', '-j-i': '-k', '-j-j': '-1', '-j-k': 'i',
    '-k1': '-k', '-ki': '-j', '-kj': 'i',  '-kk': '1',  '-k-1': 'k', '-k-i': 'j',  '-k-j': '-i', '-k-k': '-1'  
}

def analyze(string):
    result = ''
    for c in string:
        result += c
        result = table.get(result, result)

    return result

filename = 'C-small-attempt1.in' if len(sys.argv) == 1 else sys.argv[1]
with open(filename, 'r', encoding = 'shift_jis') as f:
    T = int(f.readline()[:-1])
    for t in range(T):
        L, X = [int(s) for s in f.readline()[:-1].split()]
        s = f.readline()[:-1] * X

        if (len(s) < 3):
            print('Case #{0}: {1}'.format(t + 1, 'NO'))
            continue

        slen = len(s)

        table3 = []
        max3 = slen - 2
        s3 = ''
        for i in range(max3):
            s3 = analyze(s[slen - (i + 1)] + s3)
            if s3 == 'k':
                table3.append(slen - (i + 1))
        #table3.reverse()

        result = 'NO'
        max1 = slen - 2
        s1 = ''
        for i1 in range(max1):
            s1 += s[i1]
            s1 = analyze(s1)
            if s1 != 'i':
                continue

            s2 = ''
            bi = i1 + 1
            for i3 in table3:
                if (i3 <= i1): break

                s2 += s[bi: i3]
                s2 = analyze(s2)
                bi = i3

                if s2 == 'j':
                    result = 'YES'
                    break

            if result == 'YES':
                break

        print('Case #{0}: {1}'.format(t + 1, result))
