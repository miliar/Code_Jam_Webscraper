#!/usr/bin/python

T = int(raw_input())

for t in range(T):
    Smax, S = (raw_input().split(' ')) # I think Smax is a convenience we could get from S, but we can equally conveniently use slicing
    S = [int(i) for i in S]
    cumulative = [S[0]]
    for i in S[1:]:
        cumulative.append(cumulative[-1]+i)
    # each friend will have shyness max(0, i-1) because it's all the same
    friends = 0
    for i in range(1, len(cumulative)):
        if cumulative[i-1] < i:
            friendsAdded = i - cumulative[i-1]
            friends += friendsAdded
            for c in range(i, len(cumulative)):
                cumulative[c] += friendsAdded 
    print "Case #{}: {}".format(t+1, friends)
