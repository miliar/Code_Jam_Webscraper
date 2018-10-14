import sys
from string import ascii_lowercase

samples = [("ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand"),
           ("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities"),
           ("de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up"),
           ("y qee", "a zoo")
          ]

table = {}
for a, b in samples:
    for chg, che in zip(a, b):
        table[chg] = che

alpg, alpe = '', ''
for chg, che in table.iteritems():
    alpg += chg
    alpe += che

ascii_lowercase = set(ascii_lowercase)
alpg = ascii_lowercase.difference(alpg)
alpe = ascii_lowercase.difference(alpe)

if len(alpg) == 1:
    table[alpg.pop()] = alpe.pop()

def tr(ch):
    che = table.get(ch)
    return ch if che is None else che

def trstr(astr):
    return ''.join(tr(ch) for ch in astr)

for strg, stre in samples:
    if trstr(strg) != stre:
        print strg
        print stre

def main():
    f = open(sys.argv[1])
    T = int(f.readline())
    
    for t in range(1, T+1):
        astr = f.readline()#.strip()
        print "Case #%d: %s" % (t, trstr(astr)),

if __name__ == "__main__":
    main()