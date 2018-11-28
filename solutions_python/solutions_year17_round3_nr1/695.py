filename = "A-small-attempt0.in"
outf = file(filename + ".out", "w")
rows = [i.strip() for i in file(filename).readlines()]
print rows
import math
import numpy as np


def get_row():
    global rows
    temp = rows[0]
    rows = rows[1::]
    return temp



num_cases = int(get_row())
print num_cases


def calc_surface_pankake(pankake):
    R = pankake[0]
    H = pankake[1]
    return math.pi * R**2 + 2*math.pi*R*H

def calc_total_surface(pankakes):
    max_R = max(map(lambda  t: t[0], pankakes))
    height = sum(map(lambda  t: 2*math.pi*t[0]*t[1], pankakes))
    ret = height + math.pi*max_R**2
    return ret

def process(pankakes, N, K):
    pankakes_height = []
    for pankake in pankakes:
        pankakes_height.append((pankake[0],pankake[1],calc_surface_pankake(pankake)))

    ret_pan = []
    for i in range(K):
        calcs = map(lambda t: calc_total_surface(ret_pan + [t]),pankakes)
        ret_pan.append(pankakes[np.argmax(calcs)])
        pankakes.remove(pankakes[np.argmax(calcs)])
    print calc_total_surface(ret_pan)
    return calc_total_surface(ret_pan)


for i in range(num_cases):
    #parse case
    N, K = get_row().split(" ")
    N = int(N)
    K = int(K)

    max_steps = 0
    pankakes = []

    for j in range(N):
        R, H = get_row().split(" ")
        R = int(R) * 1.0
        H = int(H) * 1.0
        pankakes.append((R,H))
    val = process(pankakes,N,K)
    outf.write("Case #" + str(i+1) + (": %06f" % (val)) + "\n")

