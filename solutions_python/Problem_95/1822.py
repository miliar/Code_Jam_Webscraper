import sys

# helpers

readline = sys.stdin.readline

# build googlerese mapping

mapping = {}

# part 1: example cases

IN = '''ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv'''

OUT = '''our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up'''

for a, b in zip(IN, OUT):
    mapping[a] = b


# part 2: hint

mapping['z'] = 'q'

# part 3: bijection property

alphabet = set("abcdefgijklmnopqrstuvwxyz")
missing_keys = list(alphabet - set(mapping.keys()))
missing_values = list(alphabet - set(mapping.values()))

assert len(missing_keys) == 1
assert len(missing_values) == 1

mapping[missing_keys[0]] = missing_values[0]

# process input

num_cases = int(readline().strip())

for i in range(1, num_cases + 1):
    line = readline().strip()
    print "Case #{0}: {1}".format(i, ''.join(map(mapping.get, line)))

