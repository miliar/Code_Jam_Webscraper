import sys

IN = [
    'ejp mysljylc kd kxveddknmc re jsicpdrysi',
    'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
    'de kr kd eoya kw aej tysr re ujdr lkgc jv',
]
OUT = [
    'our language is impossible to understand',
    'there are twenty six factorial possibilities',
    'so it is okay if you want to just give up',
]

chars = {'a': 'y', 'o': 'e', 'z': 'q'}

for i in range(3):
    X = IN[i]
    Y = OUT[i]
    for j in range(len(X)):
        chars[X[j]] = Y[j]


A =  set(chars.keys()).difference(set(chars.values()))
B =  set(chars.values()).difference(set(chars.keys()))

if len(A) == 1 and len(B) == 1:
    chars[B.pop()] = A.pop()


def convert(s):
    return ''.join(map(lambda x : chars[x], list(s)))

lines = sys.stdin.read().split("\n")
count = lines[0]

i = 1
for s in lines[1:-1]:
    print "Case #%d: %s" % (i, convert(s))
    i += 1
