from datetime import datetime
import math
from decimal import *
import copy

input_file_path = 'A-large.in.txt'

start = datetime.now()


def compute(n,k,r,h):
    rh = []

    for i in range(0,len(r)):
        rh.append(r[i]*h[i])

    area_max = 0
    for i in range(0,len(r)):
        temprh = copy.deepcopy(rh)
        area = Decimal(r[i]*r[i] + 2*temprh[i])
        temprh.pop(i)
        temprh = sorted(temprh, reverse=True)
        for j in range(0, k - 1):
            area = area + Decimal(2 * temprh[j])
        if area_max<area:
            area_max = area
    return Decimal(area_max) * Decimal(math.pi)



# def compute(n,k,r,h):
#     rh = []
#     arr = []
#
#     for i in range(0,len(r)):
#         rh.append(r[i]*h[i])
#         arr.append(r[i]*r[i] + 2*r[i]*h[i])
#
#     maxr = max(arr)
#     maxrindex = [i for i, j in enumerate(arr) if j == maxr][0]
#
#     area = Decimal(arr[maxrindex])
#     rh.pop(maxrindex)
#     rh = sorted(rh, reverse=True)
#     for i in range(0,k-1):
#         area = area + Decimal(2*rh[i])
#     area = Decimal(area) * Decimal(math.pi)
#
#     return area

    # minr = min(r)
    # minindex = -1
    # indexes = [i for i, j in enumerate(r) if j == minr]
    # if len(indexes)>1:
    #     maxh=0
    #     for i in indexes:
    #         if h[i]>maxh:
    #             maxh = h[i]
    #             minindex = i
    # else:
    #     minindex = indexes[0]


with open(input_file_path) as f:
    lines = f.read().splitlines()
    cases = int(lines[0])
    j=1
    case = 1
    while case<cases+1:
        n = int(lines[j].split(' ')[0])
        k = int(lines[j].split(' ')[1])
        r = []
        h = []
        for i in range(j+1,j+n+1):
            r.append(int(lines[i].split(' ')[0]))
            h.append(int(lines[i].split(' ')[1]))
        j = j+n+1
        output = compute(n,k,r,h)
        print 'Case #' + str(case) + ': ' + str(output)
        case = case+1


diff = datetime.now() - start
#print diff