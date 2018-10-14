import sys


def find_games(nrounds, miss, costs):
    nteams = 2**nrounds
    # rounds[i] is a list of the game numbers that team i can potentially play in
    rounds = [[] for _ in xrange(nteams)]
    for i in xrange(nteams):
        game = i
        for _ in xrange(nrounds):
            game = game // 2
            rounds[i].append(game)
            
    tickets = set()
    # buy higher-round games first
    for t in xrange(nteams):
        needed = nrounds - miss[t]
        r = nrounds-1
        while needed>0:
            tickets.add((r,rounds[t][r]))
            needed -= 1
            r -= 1
            
    return sum(costs[g[0]][g[1]] for g in tickets)

infile = sys.stdin
ntests = int(infile.readline().strip())        
for i in xrange(ntests):
    P = int(infile.readline().strip())
    miss = map(int, infile.readline().strip().split())
    costs = []
    for _ in xrange(P):
        costs.append(map(int, infile.readline().strip().split()))
        
    result = find_games(P, miss, costs)
    print("Case #%d: %d" % (i+1, result))