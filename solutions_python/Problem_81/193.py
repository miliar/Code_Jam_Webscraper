def get_stats(s):
    wins = s.count('1')
    games = wins + s.count('0')
    WP = float(wins) / games
    OWPw = float(wins) / (games-1)
    OWPl = float(wins-1) / (games-1)
    l = list(s)
    return (l, WP, OWPw, OWPl) 

def rl(f):
    return f.readline().strip()

def main():
    inp = open("A-large.in")
    out = open("A-large.out", "w")
    
    T = int(rl(inp))
    for c in range(1, T+1):
        N = int(rl(inp))
        stats = []
        for t in range(N):
            stats.append(get_stats(rl(inp)))
        
        wl = lambda t, i: 2 if stats[t][0][i] == '1' else 3
        print >>out, "Case #%d:" % c
        more_stats = []
        for t in range(N):
            team = stats[t]
            OWP = [stats[i][wl(t, i)] for i in range(N) if i != t and team[0][i] in '01']
            OWP = float(sum(OWP)) / len(OWP)
            more_stats.append((team[0], team[1], OWP))
        
        for t in range(N):
            team = more_stats[t]
            OOWP = [more_stats[i][2] for i in range(N) if i != t and team[0][i] in '01']
            OOWP = float(sum(OOWP)) / len(OOWP)
            print >>out, (team[1]*.25 + team[2]*.5 + OOWP*.25)
    
    inp.close()
    out.close()

if __name__ == '__main__':
    main()