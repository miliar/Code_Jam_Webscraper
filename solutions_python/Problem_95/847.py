#!/usr/bin/env python3

d = {
    'q': 'z',
    'e': 'o',
    'y': 'a',
    'z': 'q'
}
def mkdict():

    for line in open('./A.known.in'):
        [s1, s2] = line.split(' -> ')

        for i in range(len(s1)):
            d[s1[i]] = s2[i]

    """
    print('d = {')
    for k in sorted(d): print('\'' + k + '\': \'' + d[k] + '\'')
    print('}')
    """

def tr(s):
    t = list()
    for i in range(len(s)):
        t.append(d[s[i]])
    return ''.join(t)


def main():
    T = int(input())
    for t in range(1, T+1):
        s = input()
        print('Case #' + str(t) + ': ' + tr(s))

mkdict()
main()
