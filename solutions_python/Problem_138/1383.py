import sys
from collections import deque

def ken_strategy(blocks_n, blocks_k):
    # If Ken can just beat a block, do so. Otherwise discard a crap block
    deque_n = deque(sorted(blocks_n, reverse=True))
    deque_k = deque(sorted(blocks_k, reverse=True))

    score_n = 0
    score_k = 0

    # I don't think it matters what order we go in, so start from the heaviest
    while deque_n:
        block_n = deque_n.popleft()
        if deque_k[0] > block_n:
            deque_k.popleft()
            score_k += 1
        else:
            deque_k.pop()
            score_n +=1

    return score_n, score_k


def naomi_strategy(blocks_n, blocks_k):
    # Induce Ken to play low blocks, but then only *just* beat them.
    deque_n = deque(sorted(blocks_n, reverse=True))
    deque_k = deque(sorted(blocks_k, reverse=True))

    score_n = 0
    score_k = 0

    while deque_n:
        if deque_n[len(deque_n) - 1] < deque_k[len(deque_k) - 1]:
            # Naomi has an outright loser; make Ken play high
            deque_n.pop()
            deque_k.popleft()
            score_k += 1
        elif deque_n[len(deque_n) - 1] > deque_k[len(deque_k) - 1]:
            # Naomi declares high for Ken to play low, but then *just* beat Ken's brick
            deque_n.pop()
            deque_k.pop()
            score_n += 1

    return score_n, score_k
    

if __name__ == "__main__":
    num_cases = int(sys.stdin.readline().strip())
    for c_n in xrange(num_cases):
        num_blocks = int(sys.stdin.readline().strip())
        blocks_n = map(float, sys.stdin.readline().strip().split())
        blocks_k = map(float, sys.stdin.readline().strip().split())
        naomi_war_score, _ = ken_strategy(blocks_n, blocks_k)
        naomi_deceitful_war_score, _ = naomi_strategy(blocks_n, blocks_k)

        print "Case #%d: %d %d" % (c_n + 1, naomi_deceitful_war_score, naomi_war_score)
