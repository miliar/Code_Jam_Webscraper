basename = "B-small-attempt1"
infile = file(basename + ".in")
outfile = open(basename + ".out", "w")

def read_prices(P):
    games = []
    for p in xrange(P):
        prices = map(int, infile.readline().split())
        #print prices
        assert len(prices) == 2 ** (P - p - 1)
        for price in prices:
            assert price == 1
        games.append([False] * len(prices))
    return games

def print_tree(G):
    for row in G:
        outfile.write(" ".join(["%-5s" % g for g in row]) + "\n")

def fill_tree(M, G, r):
    # round 0: first round
    # round len(G)-1: final round (one game)

    games_to_consider = r
    games_in_round = len(G[r])
    for game_ix in xrange(games_in_round):
        num_teams = 2 ** (r + 1)
        first_team = game_ix * num_teams
        tickets_already_bought = 0
        later_game_ix = game_ix
        games_left = r + 1
        for later_round_ix in xrange(r + 1, len(G)):
            later_game_ix = later_game_ix / 2
            if G[later_round_ix][later_game_ix]:
                tickets_already_bought += 1
        for team_ix in xrange(first_team, first_team + num_teams):
            tickets_needed = (len(G) - M[team_ix]) - tickets_already_bought
            assert tickets_needed <= games_left
            #if tickets_needed == games_left:
            if tickets_needed > 0:
                G[r][game_ix] = True
                break

    #print_tree(G)
    
    if r > 0:
        fill_tree(M, G, r-1)

def count_tickets(G):
    tickets = 0
    for r in G:
        for game in r:
            if game:
                tickets += 1
    return tickets
        
def runcase(casenum):
    P = int(infile.readline())
    M = map(int, infile.readline().split())
    G = read_prices(P)

    fill_tree(M, G, len(G) - 1)
    
    outfile.write("Case #%d: %d\n" % (casenum, count_tickets(G)))

C = int(infile.readline())
for c in range(1, C+1):
    runcase(c)
