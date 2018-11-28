# Python 2.6.5

in_sample = """
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
"""

out_sample = """
our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up
"""

D = {}
D[' '] = ' '
D['q'] = 'z' # from example in statement

for i in range(len(in_sample)):
    if not in_sample[i].isalpha():
        continue
    else:
        D[in_sample[i]] = out_sample[i]

#for k in sorted(D.keys()):
#    print k, D[k]

D['z'] = 'q' # only missed letters



case_num = int(raw_input())

for t in range(1, case_num + 1):
    s = raw_input().strip()
    ns = [D[c] for c in s]
    print "Case #%d:" % t, "".join(ns)


