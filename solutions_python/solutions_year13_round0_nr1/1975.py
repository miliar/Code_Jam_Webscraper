class Game:
    def __init__(self, idx, cases):
        self.idx = idx
        self.cases = cases

    def winner(self):
        if self.cases[-1] == '':
            self.cases = self.cases[:-1]
        def wins_subset(subs):
            if len(subs) != 4:
                print "DAFUQ?"
            if subs.count('X') == 4:
                return 'X'
            if subs.count('O') == 4:
                return 'O'
            if subs.count('T') == 1:
                if subs.count('X') == 3:
                    return 'X'
                if subs.count('O') == 3:
                    return 'O'
            return None
        # Each Row
        for row in self.cases:
            val = wins_subset(row)
            if val:
                return val + " won"
        # Each Column
        for c in range(0, 4):
            col = []
            for i in range(0, 4):
                col.append(self.cases[i][c])
            val = wins_subset(col)
            if val:
                return val + " won"
        # The diagonals
        main_diag = []
        for i in range(0, 4):
            main_diag.append(self.cases[i][i])
        val = wins_subset(main_diag)
        if val:
            return val + " won"
        opp_diag = []
        for i in range(0, 4):
            opp_diag.append(self.cases[3-i][i])
        val = wins_subset(opp_diag)
        if val:
            return val + " won"
        # check for a draw (No empty zones and none of this winning cases above
        # have been matched
        is_drawn = True
        for row in self.cases:
            if row.count('.') > 0:
                is_drawn = False
                break
        if is_drawn:
            return "Draw"
        return "Game has not completed"

lines = list(open("input.dat"))
lines = map(lambda x: x.rstrip(), lines)
N = int(lines[0])
lines = lines[1:]
games = []
k = 1
for i in range(0, N):
    idx = i * 5
    games.append(Game(k, lines[idx:idx+5]))
    k += 1

for g in games:
    print "Case #" + str(g.idx) + ": " + g.winner()
