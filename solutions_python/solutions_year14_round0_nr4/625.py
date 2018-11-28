#!/usr/bin/python3

# Ken's optimal strategy is to choose the block with the lowest value above C_N... right?
# If unavailable, play the lowest block available
# What's the advantage of Naomi's strategy? Waste all of Ken's blocks so he has no answers at the end...?

# What's Naomi's standard optimal strategy? count up or count down?
# almost certainly count up, so Ken has losing blocks left at the end

# Improved strategy is... use low value blocks to take out Ken's high value blocks, then clean up with the rest
# So... start with Naomi's lowest blocks, count up until all Ken's unbeatable blocks are gone, then clean up for points

# N 0.1 0.5 0.9
# K 0.3 0.4 0.6

# Honest:
# 0.1 -> 0.3
# 0.5 -> 0.6
# 0.9 -> 0.4 (+1)

# Deceitful: 
# cancel 0.1 -> 0.6
# play 0.9 -> take out 0.4 (+1)
# play 0.5 -> take out 0.3 (+1)
# -> 2 points

### Points can only be taken once all of Ken's otherwise unbeatable blocks have been cleaned up
# 0.1 0.2 0.3 <-> 0.4 0.5 0.6, nothing can be done
# 0.1 0.2 0.4 <-> 0.3 0.5 0.6, honest is guaranteed to be 0, deceitful would be... 1?
    # Of course, the number is bound by the number of points that can _actually_ be won, i.e. number of blocks Naomi
    # holds that can beat one of Ken's

# Hrm, consideration on the honest side: if Naomi skips over one of Ken's blocks, it'll get added to points

# 9 blocks!
#N  [0.186, 0.3, 0.389, 0.557, 0.832, 0.899, 0.907, 0.959, 0.992]
#K  [0.215, 0.271, 0.341, 0.458, 0.52, 0.521, 0.7, 0.728, 0.916]
# Naomi should reach 8 points
# 0.182 -> 0.916
# 0.992 -> 0.728
# 0.959 -> 0.907...
# Ahh... deceitful is wrong
# Consider Ken's highest available block
# Can be beaten -> take it
# Can't be beaten -> burn lowest block

# Calculation blowout case: hrm, it's all list functions...
# deceitful should be fine, honest is slowest if it doesn't get to loop kb[0] < x, so continual cancels 1-1... so ken is
# above naomi the whole way

# Uhhh, unless I'm doing something dumb this is still fast... is it really a blowout?
# ehh, it's linear time, how bad could it be?

from copy import copy

def debug(*args, **kwargs):
    #print(*args, **kwargs)
    pass

def deceitful(nb, kb):
    score = 0
    while(nb):
        if nb[-1] > kb[-1]:
            del nb[-1]
            score += 1
        else:
            del nb[0]
        del kb[-1]

    return score

# nb and kb are sorted!
def deceitful2(nb, kb):
    # First dodgy step, count up on Naomi's side and down on Ken's side until ...?
        # Naomi's lowest block is above Ken's highest block?
    while nb[0] < kb[-1]:
        del nb[0]
        del kb[-1]
        if not nb:
            return 0

    return len(nb)

def honest(nb, kb):
    score = 0
    nl = len(nb)
    for x in nb:
        debug("Naomi: %s" % x)
        while kb[0] < x:
            debug("Naomi score (leftover): %s" % kb[0])
            del kb[0]
            nl -= 1 # The loop should never actually reach whatever this was pointing at...
            score += 1
            if not kb:
                debug("kb empty (cancelling)")
                return score + nl
        debug("Ken plays(win): %s" % kb[0])
        del kb[0]
        if not kb:
            debug("kb empty. score: %s nl: %s" % (score, nl))
            # -1 correction for the current (losing) block
            return score + nl - 1
        nl -= 1

    debug("nb empty")
    return score

cases = int(input())

for case in range (1, cases + 1):
    blocks = int(input())
    nb = sorted([float(x) for x in input().split()])
    debug(nb)
    kb = sorted([float(x) for x in input().split()])
    debug(kb)
    dodgy = deceitful(copy(nb), copy(kb))
    clean = honest(nb, kb)

    print("Case #%s: %s %s" % (case, dodgy, clean))
