import os

def getPoints(block_A, block_B):
    points = 0
    cur_block_B = 0

    for block_w in block_A:
        if block_w > block_B[cur_block_B]:
            points += 1
            cur_block_B += 1
    
    return points

f = open("D-large.in", 'r')

n_cases = int(f.readline().strip())

for i in xrange(1, n_cases + 1):
    num = int(f.readline().strip())
    block_Naomi = []
    block_Ken = []
    for w in f.readline().strip().split():
        block_Naomi.append(float(w))
    for w in f.readline().strip().split():
        block_Ken.append(float(w))
    block_Naomi.sort()
    block_Ken.sort()
    print "Case #{0}: {1} {2}".format(i, getPoints(block_Naomi, block_Ken), num - getPoints(block_Ken, block_Naomi))


