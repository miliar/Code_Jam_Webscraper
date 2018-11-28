def solve(s):
    return ''.join(map(inverse.get,s))

examples = \
  [ ('a zoo', 'y qee')
  , ('our language is impossible to understand', 'ejp mysljylc kd kxveddknmc re jsicpdrysi')
  , ('there are twenty six factorial possibilities', 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd')
  , ('so it is okay if you want to just give up', 'de kr kd eoya kw aej tysr re ujdr lkgc jv')
  ]
inverse = {}
for (in_,out) in examples:
    for (i,o) in zip(in_,out):
        inverse[o] = i
# import string
# set(string.lowercase) - set(inverse.keys()) = z
# set(string.lowercase) - set(inverse.values()) = q
inverse['z'] = 'q'

T = input()
for case in xrange(1,T+1):
    in_ = raw_input()
    print "Case #%s: %s" % (case, solve(in_))
#print inverse
