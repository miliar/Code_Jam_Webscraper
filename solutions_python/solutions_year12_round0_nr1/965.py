inputs = """a zoo
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv"""
outputs = """y qee
our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up"""
alpha = "abcdefghijklmnopqrstuvwxyz"
mapping = dict(zip(inputs,outputs))
#print (set(alpha)-mapping.keys())
#print (set(alpha)-set(mapping.values()))
mapping['q'] = 'z'

n = int(input())
for t in range(n):
    s = "".join(mapping[c] for c in input())
    print ("Case #%d: %s" % (t+1, s))
