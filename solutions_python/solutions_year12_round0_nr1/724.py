import sys

encoded="""ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv"""

decoded="""our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up"""

f = dict()

# learn
for a, b in zip(encoded, decoded):
    f[a] = b
f['q'] = 'z'
f['z'] = 'q'
f[' '] = ' '

"""
for i in range(26):
    c = chr(i + ord('a'))
    if c not in f.keys():
        print("Warning: %c never occured in keys!" % c)
    if c not in f.values():
        print("Warning: %c never occured in values!" % c)    
"""

T = int(sys.stdin.readline())

for testCase in range(1, T+1):
    print("Case #%i:" % testCase, "".join(f[x] for x in sys.stdin.readline().strip()))
