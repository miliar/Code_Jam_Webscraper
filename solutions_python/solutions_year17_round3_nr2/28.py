from __future__ import division

from sys import stdin, stdout
from basics import *

def solve(Ac, Aj, C_acts, J_acts):
    C_baby, J_baby = J_acts, C_acts

    C_total = sum([shift[1]-shift[0] for shift in C_baby])
    J_total = sum([shift[1]-shift[0] for shift in J_baby])

    all_shifts = []
    for shift in C_baby:
        all_shifts.append((shift[0], shift[1], "C"))
    for shift in J_baby:
        all_shifts.append((shift[0], shift[1], "J"))

    all_shifts.sort()
    all_shifts_loop = all_shifts + [all_shifts[0]]

    C_pref = []
    J_pref = []
    free = 0
    swaps = 0
    for shift, next_shift in zip(all_shifts_loop[:-1], all_shifts_loop[1:]):

        duration = next_shift[0] - shift[1]
        if duration < 0:
            duration += 1440

        if shift[-1] == next_shift[-1]:
            if duration:
                if shift[-1] == "C":
                    C_pref.append(duration)
                else:
                    J_pref.append(duration)

        else:
            swaps += 1
            free += duration

    C_pref.sort()
    J_pref.sort()

    if C_total < 720:
        while C_pref and (C_total < 720):
            pref_time = C_pref.pop(0)
            if pref_time + C_total <= 720:
                C_total += pref_time

            elif (pref_time + C_total) > 720:
                C_pref.insert(0, pref_time - (720 - C_total))
                C_total = 720
                break

    if J_total < 720:
        while J_pref and (J_total < 720):
            pref_time = J_pref.pop(0)
            if pref_time + J_total <= 720:
                J_total += pref_time

            elif (pref_time + J_total) > 720:
                J_pref.insert(0, pref_time - (720 - J_total))
                J_total = 720
                break

    # print C_baby
    # print J_baby
    # print C_total
    # print J_total
    # print C_pref
    # print J_pref
    # print free

    return swaps + 2 * (len(C_pref) + len(J_pref))
    

T = read_val()

for t in range(T):
    Ac, Aj = read_vals()
    C_acts = read_lines(Ac)
    J_acts = read_lines(Aj)

    result = solve(Ac, Aj, C_acts, J_acts)

    stdout.write("Case #{}: {}\n".format(t+1, result))