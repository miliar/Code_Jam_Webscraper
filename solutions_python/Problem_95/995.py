#!/usr/bin/env python
from sys import stdin

mapping = {}
#mapping['a'] = 'y'
#mapping['o'] = 'e'
mapping['z'] = 'q'
mapping['q'] = 'z'

src = 'ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv'

dest = 'our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up'

for i  in range(len(src)):
    if src[i] not in mapping:
        mapping[src[i]] = dest[i]

#for l in 'abcdefghijklmnopqrstuvwxyz ':
#    if l not in mapping: print 's ' + l
#    if l not in dest: print 'd ' + l



def main():
    no_cases = int(stdin.readline())
    for case in range(no_cases):
        src = stdin.readline().replace('\n', '')
        dest = []
        missing = []
        for i, c in enumerate(src):
            if c in mapping:
                dest.append(mapping[c])
            else:
                print c + ' missing'
                dest.append('*')
                missing.append[i]
        dest = ''.join(dest)
        print 'Case #%d: %s' % (case+1, dest)
        

if __name__ == '__main__':
    main()
