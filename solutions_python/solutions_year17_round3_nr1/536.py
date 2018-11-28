from Codejam import codejam_run, line as l
from math import pi

inf = float("inf")

def A_top(r):
    return r * r * pi

def A_mantle(r, h):
    return 2 * pi * r * h

@codejam_run(l(N=int, K=int),\
             l(times="N", array_name="pcs"))
def solve(N, K, pcs):
    pcs = [tuple(pc) for pc in pcs]

    max_exposed = 0

    for i, bottom_pc in enumerate(pcs):
        br, bh = bottom_pc
        bottom_pc_size = A_top(br) + A_mantle(*bottom_pc)

        rest_pcs = pcs[:i] + pcs[i+1:]
        rest_pcs = [(r, h) for r, h in rest_pcs if r <= br]

        rest_pcs_Am = [A_mantle(*pc) for pc in rest_pcs]
        rest_pcs_Am.sort()
        rest_pcs_Am.reverse()

        max_exposed = max(bottom_pc_size + sum(rest_pcs_Am[:K-1]), max_exposed)

    return " " + str(max_exposed)
