import ast
import string

d = {'a': 'y', 'o': 'e', 'z': 'q'}

# Test data
d.update(zip("our language is impossible to understand", "ejp mysljylc kd kxveddknmc re jsicpdrysi"))
d.update(zip("there are twenty six factorial possibilities", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"))
d.update(zip("so it is okay if you want to just give up", "de kr kd eoya kw aej tysr re ujdr lkgc jv"))

# Last datum (since d is a bijection)
lower = set(string.lowercase)
[k], [v] = lower - set(d.keys()), lower - set(d.values())
d[k] = v

r = {v: k for k, v in d.items()}

for i in range(1, ast.literal_eval(raw_input())+1):
    print "Case #{0}: {1}".format(i, "".join(r[c] for c in raw_input()))
