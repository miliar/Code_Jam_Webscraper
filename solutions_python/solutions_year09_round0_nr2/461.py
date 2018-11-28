#!/usr/bin/python

"""
  Google Code Jam 2009
  philfifi@free.fr
  All rigths reserved
"""

from math import sqrt
from decimal import *
getcontext().prec = 100

import psyco
psyco.full()

_debug = 0

FLOW_TO_N = 1
FLOW_TO_W = 2
FLOW_TO_E = 3
FLOW_TO_S = 4
SINK = 0

MAX_ALT = 10000

def mark_flowing_on_me(h_me, w_me, mark, table):
    pass


def solve_case(case_no,  H, W, altitudes_l   ):
    print "-------------- New case", case_no

    start_val = "."

    resuls_l = [None] * H
    flow_to_l = [None] * H
    flow_from_l = [None] * H
    for _ in range(H):
        resuls_l[_] = [start_val] * W
        flow_to_l[_] = [None] * W
        flow_from_l[_] = [ None ] * W

    for h in range(H):
        for w in range(W):
            flow_from_l[h][w] = []


    # Sort by altitudes:
    # -------------------
    altitudes_coords_l = [None] * (H*W)
    index = 0
    for h in range(H):
        for w in range(W):
            altitudes_coords_l[index] = (altitudes_l[h][w],
                                         (h,w))
            index += 1

    altitudes_coords_l.sort(key=lambda x:x[0])


    sink_l = []  # (altitude, (h,w) )
    # flow to map:
    for h in range(H):
        for w in range(W):
            my_alt = altitudes_l[h][w]
            # Get neighbourg altitudes
            if h == 0:
                cell_up_alt = MAX_ALT
            else:
                cell_up_alt = altitudes_l[h-1][w]

            if w == 0:
                cell_left_alt = MAX_ALT
            else:
                cell_left_alt = altitudes_l[h][w-1]

            if h == H-1:
                cell_down_alt = MAX_ALT
            else:
                cell_down_alt = altitudes_l[h+1][w]

            if w == W-1:
                cell_right_alt = MAX_ALT
            else:
                cell_right_alt = altitudes_l[h][w+1]

            # Where does it flow ?
            smallest_alt = None
            smallest_flow = SINK

            if cell_down_alt<my_alt:
                smallest_alt = cell_down_alt
                smallest_flow = FLOW_TO_S
            if cell_right_alt<my_alt and (smallest_alt is None or
                                          cell_right_alt <= smallest_alt):
                smallest_alt = cell_right_alt
                smallest_flow = FLOW_TO_E
            if cell_left_alt<my_alt and (smallest_alt is None or
                                          cell_left_alt <= smallest_alt):
                smallest_alt = cell_left_alt
                smallest_flow = FLOW_TO_W
            if cell_up_alt<my_alt and (smallest_alt is None or
                                       cell_up_alt <= smallest_alt):
                smallest_alt = cell_up_alt
                smallest_flow = FLOW_TO_N



            if smallest_flow == FLOW_TO_N:
                flow_from_l[h-1][w].append((h,w))
            elif smallest_flow == FLOW_TO_W:
                flow_from_l[h][w-1].append((h,w))
            elif smallest_flow == FLOW_TO_E:
                flow_from_l[h][w+1].append((h,w))
            elif smallest_flow == FLOW_TO_S:
                flow_from_l[h+1][w].append((h,w))
            else:
                sink_l.append( (my_alt, (h,w)) )
            flow_to_l[h][w] = smallest_flow


#    print "flow_to", flow_to_l

    print '%d sinks' % len(sink_l)
#    print sink_l

#    print "flow_from_l:", flow_from_l

    mark = "A"
    for alt, coord in sink_l:
        # Who is flowing on me ?
        h, w = coord

        to_follow_l = []

        resuls_l[h][w] = mark
        to_follow_l += flow_from_l[h][w]

        while to_follow_l:
            #get an item to follow
            h, w = to_follow_l.pop(0)
#            print "go to", h, w
            resuls_l[h][w] = mark
            to_follow_l += flow_from_l[h][w]
#            print "add", len(flow_from_l[h][w])


        mark = chr(ord(mark) +1)

    # remap the resuls
    remap_d = {}
    mark = "a"
    for w in range(W):
        for h in range(H):
            char_in = resuls_l[h][w]
            if char_in not in remap_d:
                remap_d[char_in] = mark
                mark = chr(ord(mark) +1)


    # Format the output
    resuls_remaped_l = []
    for line in resuls_l:
        line_l = []
        for char in line:
            line_l.append(remap_d[char])

        resuls_remaped_l.append(line_l)

    out_str1 = [ " ".join(line) for line in resuls_remaped_l ]
    out_str2 = "\n".join(out_str1)

    return out_str2


def main(argv):

    f_out_name = argv[1].split(".")[0] + ".out"
    f_out = open(f_out_name, "w")

    fd = open(argv[1])
    nb_cases = int(fd.readline())


    for case_no in range(1, nb_cases+1):

        H, W = [int(item) for item in fd.readline().split()]

        altitudes_l = []
        for _ in range(H):
             altitudes_l.append( [int(item) for item in fd.readline().split()] )


        # Have read all stuff for this case:
        f_out.write( "Case #%d:\n%s\n" % (case_no,
                                         solve_case(case_no, H, W, altitudes_l)
                                         )
                     )
        f_out.flush()

    f_out.close()

    for line in open(f_out_name):
        print line,



import sys
if __name__ == "__main__":
    main(sys.argv)
