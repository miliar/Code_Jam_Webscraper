import sys, itertools

mapping = {'y': 'a', 'e': 'o', 'q': 'z'}

inputs = """
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
"""

outputs = """
Case #1: our language is impossible to understand
Case #2: there are twenty six factorial possibilities
Case #3: so it is okay if you want to just give up
"""

for _input, _output in zip(inputs.strip().splitlines(), outputs.strip().splitlines()):
    _i = _input.strip()
    _o = _output[_output.index(":")+1:].strip()
    
    mapping.update(zip(_i, _o))

print(":".join("{0[0]} {0[1]}".format(m) for m in mapping.items()))

