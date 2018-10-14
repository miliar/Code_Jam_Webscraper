"""
I woke up a bit this time. If I get to the next round I won't be doing it on 48 hours of awakeness... eugh

"""

# Build map of Googlerese to English from the examples
example_in  = list('ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv y e q z')
example_out = list('our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up a o z q')
map = {}
for i, c in enumerate(example_in):
    map[c] = example_out[i]

file = 'A-small-attempt4'

with open(file + '.in', 'r') as input:
    lines = input.readlines()

cases = []
for line in lines[1:]:
    line = list(line.strip())
    for i, c in enumerate(line):
        line[i] = map[c]
    cases.append(''.join(line))

with open(file + '.out', 'w') as output:
    for i, case in enumerate(cases):
        output.write("Case #%d: %s\n" % (i+1, case))
