import collections
import sys

inp = sys.stdin

def solve(seq):
    bot_seqs = collections.defaultdict(list)
    bot_turns = []
    for i in xrange(0, len(seq), 2):
        bot_turns.append(seq[i])
        bot_seqs[seq[i]].append(int(seq[i + 1]))
    bot_poss = dict([(b, 1) for b in bot_seqs])
    ## print '-------'
    ## print bot_turns
    ## print bot_seqs
    ## print bot_poss
    count = 0
    while len(bot_turns):
        count += 1
        next_turn_of = bot_turns[0]
        for b, p in bot_poss.iteritems():
            if b == next_turn_of:
                continue
            if not len(bot_seqs[b]):
                continue
            if p == bot_seqs[b][0]:
                continue
            if p < bot_seqs[b][0]:
                bot_poss[b] += 1
            else:
                assert p > bot_seqs[b][0]
                bot_poss[b] -= 1
        if bot_poss[next_turn_of] == bot_seqs[next_turn_of][0]:
            bot_seqs[next_turn_of].pop(0)
            bot_turns.pop(0)
        elif bot_poss[next_turn_of] < bot_seqs[next_turn_of][0]:
            bot_poss[next_turn_of] += 1
        else:
            bot_poss[next_turn_of] -= 1
    return count

T = int(inp.readline())
for i, line in enumerate(sys.stdin, 1):
    split = line.split()
    N = int(split[0])
    print 'Case #%d: %d' % (i, solve(split[1:]))

