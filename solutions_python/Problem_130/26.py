""" imports """
import glob, pprint, pickle, os, time, sys
from copy import copy
from numpy import array, sin, cos

""" global variables """

""" classes """

""" functions """
W = 1
L = 0
def doublecheck(N, P, answer):
    M = 2**N
    records = []
    for m in range(M):
        records.append([])
    for rounds in range(N):
        not_played = [m for m in reversed(range(M))]
        while not_played:
            m = not_played.pop(0)
            for mm in not_played:
                if records[mm] == records[m]:
                    ## play
                    records[m].append(L)
                    records[mm].append(W)
                    assert m > mm
                    not_played = [np for np in not_played if np != mm]
                    break
            else:
                assert False
    ranking = sorted([[records[m], m] for m in range(M)], reverse=True)
    ranking = [m for rec, m in ranking]
    prizes = ranking[:P]
    ## get ansers
    for guaranteed_prize in range(M):
        if guaranteed_prize not in prizes:
            guaranteed_prize -= 1
            break
    may_win_prize = max(prizes)
    guaranteed_prize_ans, may_win_prize_ans = answer

    assert guaranteed_prize == guaranteed_prize_ans

    print N, P, prizes, may_win_prize_ans
    assert may_win_prize == may_win_prize_ans

def solve(N, P):
    M = 2**N
    for n in range(N+10):
        if P > (2**n-1) * 2**(N-n):
            continue
        n = n - 1
        break
    guaranteed_prize = 2**(n+1)-2
    guaranteed_prize = min(guaranteed_prize, M-1)

    for n in range(N):
        if P >= 2**(N-n):
            break
    else:
        n = N
    may_win_prize = M - 2**n
    assert 0 <= may_win_prize < M
    assert 0 <= guaranteed_prize < M
    if P == M:
        assert may_win_prize == M-1
        assert guaranteed_prize == M-1
        print "PMM"
    return guaranteed_prize, may_win_prize

""" parse input """
output = ""
TIC = time.time()
with open(sys.argv[1] if len(sys.argv) > 1 else "default.in") as f:
    def read_ints():
        return [int(x) for x in f.readline().strip().split(' ')]
    (numquestions,) = read_ints()
    for questionindex in xrange(numquestions):
        ### parse input ###
        N, P = read_ints()
        ### calculate answer ###
        answer = solve(N, P)
        # doublecheck(N, P, answer)
        ### output ###
        #print "Calculating case #{}...".format(questionindex+1)
        answer_str = "Case #{}: {} {}".format(questionindex+1, *answer)
        output += answer_str + '\n'
        print answer_str
ofile = open('output', 'w').write(output)
TOC = time.time()
#print "done in {} s".format(TOC-TIC)