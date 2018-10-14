import logging
import Queue as Q
import math
import pprint

logging.basicConfig(filename='log.txt', level=logging.DEBUG)

def compute(N,K,pancakes):
    # bottom_cake = -1
    # bottom_cake_surface = -1
    # for i in xrange(N):
    #     r,h = pancakes[i]
    #     this_cake_surface = math.pi*r**2+2*math.pi*r*h 
    #     if this_cake_surface > bottom_cake_surface:
    #         bottom_cake_surface = this_cake_surface
    #         bottom_cake = i
    #
    # print pancakes[bottom_cake], bottom_cake_surface

    cake_side_faces = []
    for i in xrange(N):
        r,h = pancakes[i]
        cake_side_faces.append((2*math.pi*r*h, i))
    cake_side_faces.sort(reverse=True)
    # print cake_side_faces

    result = 0
    chosen_pancakes = set()
    cur_max_r = -1
    for i in xrange(K-1):
        result += cake_side_faces[i][0]
        if pancakes[cake_side_faces[i][1]][0] > cur_max_r:
            cur_max_r = pancakes[cake_side_faces[i][1]][0]
        chosen_pancakes.add(cake_side_faces[i][1])

    next_max_pancake = -1
    # print cur_max_r
    bottom_cake_surface = -1
    for i in xrange(N):
        if i in chosen_pancakes:
            continue
        r,h = pancakes[i]
        r_large = max(r, cur_max_r)
        this_cake_surface = math.pi*r_large**2+2*math.pi*r*h 
        if this_cake_surface > bottom_cake_surface:
            bottom_cake_surface = this_cake_surface

    result += bottom_cake_surface
    return result

t = int(raw_input())
for i in xrange(1, t + 1):
    logging.info("Solving case: {}".format(i))

    # N = int(raw_input())
    N, K = [int(x) for x in raw_input().split(" ")]
    pancakes = []
    for _ in xrange(N):
        pancakes.append([int(x) for x in raw_input().split(" ")])

    result = compute(N,K,pancakes)
    # correct_compute(grid)
    print "Case #{}: {:.10f}".format(i, result)
