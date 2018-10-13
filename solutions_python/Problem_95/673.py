from sys import stdin
import string

s_googlese = ["ejp mysljylc kd kxveddknmc re jsicpdrysi",
              "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
              "de kr kd eoya kw aej tysr re ujdr lkgc jv",
              "y qee"]
              
s_english = ["our language is impossible to understand",
             "there are twenty six factorial possibilities",
             "so it is okay if you want to just give up",
             "a zoo"]
             
trans_map = {}

for g, e in zip(s_googlese, s_english):
    for a, b in zip(g, e):
        if a in trans_map and trans_map[a] != b:
            assert False
        trans_map[a] = b
    
available_keys = list(string.lowercase + ' ')
available_vals = list(string.lowercase + ' ')

for k in trans_map.keys():
    v = trans_map[k]
    available_keys.remove(k)
    available_vals.remove(v)
    
if len(available_keys) != len(available_vals):
    assert False

if len(available_keys) > 1:
    assert False
    
if len(available_keys) == 1:
    k = available_keys[0]
    v = available_vals[0]
    trans_map[k] = v
    
    
X = map(lambda x: x.strip(), stdin.readlines())
T = int(X[0])

for t in xrange(1, T + 1):
    strans = ""
    for s in X[t]:
        if s not in trans_map:
            assert False
        strans += trans_map[s]
    print "Case #%d: %s" % (t, strans)