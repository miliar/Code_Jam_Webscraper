encrypted = """
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
y qee
"""
plain = """
our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up
a zoo
"""
alpha = set("abcdefghijklmnopqrstuvwxyz")

d = dict(zip(encrypted, plain))
missing_encr  = alpha-set(encrypted)
missing_plain = alpha-set(plain)
d[missing_encr.pop()] = missing_plain.pop()

T = int(input())
for i in range(1, T+1):
	print("Case #", i, ": ", "".join(d[e] for e in input()), sep="")
