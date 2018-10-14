#!/usr/bin/python3
m = {
    'a':'y',
    'o':'e',
    'z':'q',
    'q':'z'
}
given = (
    ('ejp mysljylc kd kxveddknmc re jsicpdrysi','our language is impossible to understand'),
    ('rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd','there are twenty six factorial possibilities'),
    ('de kr kd eoya kw aej tysr re ujdr lkgc jv','so it is okay if you want to just give up')
)

for weird, english in given:
    assert(len(weird) == len(english))
    for i in range(len(weird)):
        m[weird[i]] = english[i]

for i in range(int(input())):
    line = input()
    o = ''
    for char in line:
        o+=m[char]
    print('Case #%d: %s' % (i+1,o))
