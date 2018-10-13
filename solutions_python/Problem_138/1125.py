import sys
import os

'''
Obviously:
* optimal Ken strategy:
    * if he has blocks heavier than Naomi's, choose lightest of those
    * otherwise choose lightest of all his blocks
* optimal Naomi decent strategy:
    * play blocks from heaviest to lightest
* deceit Naomi strategy:
    * try to fake out Ken's heaviest block (giving him a point :( )
    * try to fake out Ken's lightest block (earning a point)
'''
def getKenMove(naomi, kenBlocks):
    # fast check if we can choose a heavier block than naomi
    if kenBlocks[-1] > naomi:
        # find that slightly heavier one
        for block in kenBlocks:
            if block > naomi:
                move = block
                break
    else:
        # we don't have a heavier block, choose lightest
        move = kenBlocks[0]
    kenBlocks.remove(move)
    return move

def getNaomiMove(naomiBlocks, kenBlocks):
    minBlock = kenBlocks[0]
    if naomiBlocks[-1] > minBlock:
        # we can cheat Ken on his lighest block
        fake = kenBlocks[-1] + 0.1 # fake saying we put heavier block than any that Ken has
        for block in naomiBlocks:
            if block > minBlock:
                move = block
                break
    else:
        # we try to cheat out Ken's heaviest block
        try:
            fake = 0.5 * (kenBlocks[-1] + kenBlocks[-2])
        except IndexError:
            # Ken has only 1 block left
            fake = kenBlocks[-1] - 0.1
        move = naomiBlocks[0]
    naomiBlocks.remove(move)
    return move, fake

def getDeceitScore(naomiBlocks, kenBlocks):
    score = 0
    while naomiBlocks:
        naomi, fake = getNaomiMove(naomiBlocks, kenBlocks)
        ken = getKenMove(fake, kenBlocks)
        if naomi > ken:
            score += 1
    return score

def getDecentScore(naomiBlocks, kenBlocks):
    score = 0
    while naomiBlocks:
        naomi = naomiBlocks.pop(-1)
        ken = getKenMove(naomi, kenBlocks)
        if naomi > ken:
            score += 1
    return score

def main():
    with open(sys.argv[1], 'r') as inp, open('%s.out' % (os.path.splitext(sys.argv[1])[0]), 'w') as out:
        T = int(inp.readline())
        for t in xrange(T):
            N = int(inp.readline())
            naomi = sorted(float(x) for x in inp.readline().split())
            ken = sorted(float(x) for x in inp.readline().split())
            out.write('Case #%s: %s %s\n' % (t + 1, getDeceitScore(list(naomi), list(ken)),
                                             getDecentScore(list(naomi), list(ken))))

if __name__ == '__main__':
    main()
