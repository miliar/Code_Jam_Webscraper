import fileinput
import itertools

def solve(combo, contra, spell):
    out = []
    for elem in spell:
        while out:
            pair = tuple(sorted([out[-1], elem]))
            if pair in combo:
                out.pop()
                elem = combo[pair]
            else:
                break
        if elem in contra and set(out).intersection(contra[elem]):
            out = []
        else:
            out.append(elem)
    return out

readline = fileinput.input().readline
case_count = int(readline())
for case_no in range(case_count):
    parts = readline().split()
    combo_count = int(parts.pop(0))
    combo_dict = {}
    for i in range(combo_count):
        combo = parts.pop(0)
        combo_dict[tuple(sorted(combo[0:2]))] = combo[2]
    contra_count = int(parts.pop(0))
    contra_dict = {}
    for i in range(contra_count):
        contra = parts.pop(0)
        contra_dict.setdefault(contra[0], set()).add(contra[1])
        contra_dict.setdefault(contra[1], set()).add(contra[0])
    spell = parts[-1]
    answer = solve(combo_dict, contra_dict, spell)
    print "Case #%d: [%s]" % (case_no+1, ', '.join(answer))
