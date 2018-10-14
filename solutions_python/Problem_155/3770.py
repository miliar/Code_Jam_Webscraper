#!/usr/bin/python
import sys
with open('game.txt') as f:
    content = f.readlines()[1:]
content = map(lambda s: s.strip(), content)
content = filter(None, content)
case = 1

for line in content:
    lines = line.split()
    max_shy = lines[0]
    mem_shy = lines[1]
    invite = 0
    flag_clear = 0
    same_char = 1
    ppl = 0
    shy_level = 1

    ppl = mem_shy[0]

    for mem in mem_shy[1:]:
        if int(ppl) >= int(max_shy):
            break
        if mem != '0':
            if int(ppl) >= int(shy_level):
                ppl = int(mem) + int(ppl)
                if int(ppl) >= int(max_shy):
                    break
            else:
                invite += (int(shy_level) - int(ppl))
                ppl    = int(mem) + int(ppl) + int(invite)
        shy_level += 1

    sys.stdout.write("Case #%d: %d\n" % (case , invite))
    case += 1
