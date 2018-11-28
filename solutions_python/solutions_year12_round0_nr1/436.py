table = {' ': ' ',
         'y': 'a',
         'e': 'o',
         'q': 'z'}

for g, s in [('ejp mysljylc kd kxveddknmc re jsicpdrysi',
              'our language is impossible to understand'),
             ('rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
              'there are twenty six factorial possibilities'),
             ('de kr kd eoya kw aej tysr re ujdr lkgc jv',
              'so it is okay if you want to just give up')]:
    for gch, sch in zip(g, s):
        table[gch] = sch

#print len(table)  # only 26 symbols (incl. space) -> one is missing

abc = set('abcdefghijklmnopqrstuvwxyz ')

g_missing = list(abc - set(table.keys()))[0]
s_missing = list(abc - set(table.values()))[0]

table[g_missing] = s_missing

def trans(s):
    return ''.join(table[ch] for ch in s)

with open('A-small-attempt0.in') as f:
    t = int(f.readline())
    for i in range(t):
        print 'Case #%d: %s' % (i + 1, trans(f.readline().strip()))

#print trans('rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd')
