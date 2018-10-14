import sys

class Team(object):
    def __init__(self, teamid):
        self.teamid = teamid
        self.wins = set()
        self.losses = set()
        self._owp = None
        
    def wp(self):
        return 1.0*len(self.wins) / (len(self.wins) + len(self.losses))
        
    def owp(self, teams):
        if self._owp is not None: return self._owp
        
        total = 0
        opps = self.wins.union(self.losses)
        for opp in opps:
            oppgames = (len(opp.wins)+len(opp.losses)-1)
            oppwins = len(opp.wins)
            if self in opp.wins: oppwins -= 1
            total += (1.0*oppwins/oppgames)
            
        self._owp = total/len(opps)
        return self._owp
        
    def oowp(self, teams):
        opps = self.wins.union(self.losses)
        total = sum(opp.owp(teams) for opp in opps)
        return total / len(opps)
            

def compute_rpi(team, all_teams):
    return 0.25*team.wp() + 0.5*team.owp(teams) + 0.25*team.oowp(teams)
    

infile = sys.stdin

T = int(infile.readline())
for i in xrange(T):
    N = int(infile.readline())
    teams = [Team(j+1) for j in xrange(N)]
    for team in teams:
        matches = infile.readline().strip()
        for j,ch in enumerate(matches):
            if ch=='0': team.losses.add(teams[j])
            elif ch=='1': team.wins.add(teams[j])
            
        #print("Team %s wins:%s losses:%s" % (team.teamid, ' '.join(str(t.teamid) for t in team.wins), ' '.join(str(t.teamid) for t in team.losses)))
    
    rpis = [compute_rpi(t, teams) for t in teams]
    print("Case #%d:" % (i+1))
    for rpi in rpis: print(rpi)
