#!/usr/bin/python
import math, re, collections

norm = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"
gog = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"

def read_data(T):
    data = []
    for i in range(T):
        strd = raw_input()
        data.append(strd)
    return data
    
def read_text():
    T = int(raw_input())
    return read_data(T)

def stat(text):
    stats = {}
    for c in text:
        if c == ' ':
            continue
        v = stats.setdefault(c, 0)
        stats[c] = v + 1
    return stats

def print_stat(stats, n):
    if not stats or not n:
        return
    m, mk = 0, '-'
    for k in stats.keys():
        if m < stats[k]:
            m, mk = stats[k], k
    del stats[mk]
    print m, mk
    print_stat(stats, n - 1)

tran = {'z':'q', 'q':'z'}
for i in range(len(gog)):
    tran[gog[i]] = norm[i]

data = read_text()
n = 1
for s in data:
    print "Case #%d: %s" % (n, "".join(map(lambda x: tran[x], s)))
    n += 1
