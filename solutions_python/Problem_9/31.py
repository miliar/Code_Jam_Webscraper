from collections import deque

T = int(raw_input())

for case in range(1,T+1):
    K = int(raw_input())
    deck = [None]*K
    cur_deck = range(K)

    for i in range(K):
        j = i % len(cur_deck)
        deck[cur_deck[j]] = i+1
        cur_deck = cur_deck[j+1:]+cur_deck[:j]

#    print deck

    ds = map(int, raw_input().split())[1:]

    print 'Case #%i:' % case,
    for d in ds:
        print deck[d-1],
    print
