'''
Created on 13 apr 2014

@author: algestam
'''

def default_move(blocks):
    return blocks[-1]

def only_wins_left(myblocks, otherblocks):
    for i in xrange(len(myblocks)):
        if myblocks[i] < otherblocks[i]:
            return False
    return True

def deceitful_move(myblocks, otherblocks):
    deceit = False
    selected = myblocks[0]
    if otherblocks[-1] > selected:
        deceit = True
            
    if only_wins_left(myblocks, otherblocks):
        selected = default_move(myblocks)
        deceit = True
    return selected, deceit


def normal_reply(blocks, target):
    sel = blocks[0]
    for b in blocks:
        if b > target:
            sel = b
            break
    return sel

def deceited_reply(blocks):
    return blocks[-1]

def deceitful(naomi, ken):
    naomi.sort()
    ken.sort()
    naomi_points = 0
    ken_points = 0
    while (len(naomi) > 0):
        c_n, deceited = deceitful_move(naomi, ken)
        naomi.remove(c_n)
        
        if deceited:
            c_k = deceited_reply(ken)
        else:
            c_k = normal_reply(ken, c_n)
        ken.remove(c_k)
        
        if c_n > c_k:
            naomi_points += 1
        else:
            ken_points += 1
    return naomi_points

def war(naomi, ken):
    naomi.sort()
    ken.sort()
    naomi_points = 0
    
    while (len(naomi) > 0):
        c_n = default_move(naomi)
        naomi.remove(c_n)
        c_k = normal_reply(ken, c_n)
        ken.remove(c_k)
        
        if c_n > c_k:
            naomi_points += 1
            
    return naomi_points
        
def solve(naomi, ken):
    dw = deceitful(list(naomi), list(ken))
    w = war(list(naomi), list(ken))
    
    return dw, w

for case in xrange(input()):
    num_blocks = int(raw_input())
    naomi_blocks = [float(v) for v in raw_input().split()]
    ken_blocks = [float(v) for v in raw_input().split()]
    
    dw, w = solve(naomi_blocks, ken_blocks)

    print "Case #%i: %i %i" % (case+1, dw, w)