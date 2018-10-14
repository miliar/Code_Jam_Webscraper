#!/usr/bin/env pypy
import sys, os

outfile = open("%s.out" % sys.argv[1], "w")
case_number = 1

def get_min(case):
    cc = {}
    for s in case:
        ss = [(1, s[0])]
        for c in s[1:]:
            if ss[-1][1] != c:
                ss += [(1, c)]
            else:
                last = ss[-1]
                ss[-1] = (last[0] + 1, last[1])
        mini = "".join([a[1] for a in ss])
        try:
            cc[mini] += [ss]
        except KeyError:
            cc[mini] = [ss]
    return cc
    
# def calc(case, moy):
#     moves = 0
#     reference = None
#     ecart = 0
#     index = 0
#     while reference is None:
#         for index, s in enumerate(case):
#             if len(s) == (moy - ecart) or len(s) == (moy + ecart):
#                 reference = s
#                 break
#         ecart += 1
#     for index2, s in enumerate(case):
#         if index2 != index:
#             moves += abs(len(s) - moy)
#     return moves

def solving(case):
    global case_number
    print "\n%d" % case_number
    result = None
    cc = get_min(case)
    # result = None
    # sset = get_min(case)
    if len(cc) != 1:
        result = "Fegla Won"
    elif len(set(case)) == 1:
        result = "0"
    else:
        mini, strings = cc.keys()[0], cc.values()[0]
        result = 0
        for i in range(len(mini)):
            ecarts = [s[i][0] for s in strings]
            if len(set(ecarts)) == 1:
                continue
            moy = int(round(reduce(lambda x, y: float(x) + y, ecarts) / len(ecarts)))
            print ecarts
            result += sum([abs(e - moy) for e in ecarts])
        result = str(result)
                
        # moy = sum([len(s) for s in case])/len(case)
        # origin_moy = moy
        # while True:
        #     moves = calc(case, moy)
        #     if moves != 0:
        #         break
        #     moy -= 1
        #     # assert moy >= len(sset])
        # result = str(moves + origin_moy - moy)
        
    outfile.write("Case #%d: %s\n" % (case_number, result))
    case_number += 1

with open(sys.argv[1]) as infile:
    case = []
    for l in infile.readlines()[1:]:
        l = l.strip()
        try:
            n = int(l)
        except:
            case.append(l)
        else:
            if case:
                solving(case)
            case = []

    solving(case)
    
outfile.close()
