__author__ = 'tobias'

with open('A-small-attempt0.in') as inp:
    with open('A-small-attempt0.out', 'w') as out:
        cases = inp.readline().strip()
        for case in range(int(cases)):
            first_answer = inp.readline().strip()
            first_grid = []
            for i in range(4):
                first_grid.append(inp.readline().strip().split())
            sec_answer = inp.readline().strip()
            sec_grid = []
            for i in range(4):
                sec_grid.append(inp.readline().strip().split())
            pos_cards = set(first_grid[int(first_answer) - 1]).intersection(set(sec_grid[int(sec_answer) - 1]))
            if len(pos_cards) is 1:
                output = pos_cards.pop()
            elif len(pos_cards) is 0:
                output = "Volunteer cheated!"
            else:
                output = "Bad magician!"
            out.write("Case #{case}: {out}\n".format(case=case + 1, out=output))
