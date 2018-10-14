__author__ = 'umur'

import sys
import string

c = int(sys.stdin.readline())
cases = []
solution = []
charmap = (("e", "o"), ("j", "u"), ("p", "r"), ("m", "l"), ("y", "a"), ("s", "n"), ("l", "g"), ("c", "e"), ("k", "i"),
       ("d", "s"), ("x", "m"), ("v", "p"), ("n", "b"), ("r", "t"), ("i", "d"), ("b", "h"), ("t", "w"),
       ("a", "y"), ("h", "x"), ("w", "f"), ("f", "c"), ("o", "k"), ("u", "j"), ("z", "q"), ("g", "v"), ("q", "z"), 
    )
stable = ""
ttable = ""
for s,t in sorted(charmap):
    stable = stable+s
    ttable = ttable+t
trans_table = string.maketrans(stable,ttable)

for i in range(0, c):
    cases.append(sys.stdin.readline().replace("\n",""))

for case in cases:
    solution.append(case.translate(trans_table))

for counter,sol in enumerate(solution):
    print "Case #%s: %s" % (str(int(counter)+1), sol)
