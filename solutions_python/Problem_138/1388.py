import bisect
from codejam import *

def war(noami_blocks, ken_blocks):
    blocks_num = len(noami_blocks)
    noami_points = 0
    for i in xrange(blocks_num):
        noami_block = noami_blocks.pop(0)
        if noami_block > ken_blocks[-1]:
            ken_block = ken_blocks.pop(0)
        else:
            idx = bisect.bisect_left(ken_blocks, noami_block)
            ken_block = ken_blocks.pop(idx)

        if noami_block > ken_block:
            noami_points += 1

    return noami_points

def deceitful_war(noami_blocks, ken_blocks):
    blocks_num = len(noami_blocks)
    noami_points = 0
    for i in xrange(blocks_num):
        noami_block = noami_blocks.pop(0)
        if noami_block > ken_blocks[-1] or noami_block > ken_blocks[0]:
            ken_block = ken_blocks.pop(0)
        else:
            ken_block = ken_blocks.pop()

        if noami_block > ken_block:
            noami_points += 1

    return noami_points

for i in xrange(readint()):
    blocks_num = readint()
    noami_blocks = readfloatarray()
    ken_blocks = readfloatarray()

    noami_blocks.sort()
    ken_blocks.sort()

    noami_points = deceitful_war(noami_blocks[:], ken_blocks[:])
    noami_points_real = war(noami_blocks, ken_blocks)
    print "Case #%d: %d %d" % (i + 1, noami_points, noami_points_real)
