#!/usr/bin/python

#across
generators = [lambda rows: rows[0],
              lambda rows: rows[1],
              lambda rows: rows[2],
              lambda rows: rows[3]]
#down 
generators.extend([lambda rows: (rows[y][0] for y in range(4)),
                   lambda rows: (rows[y][1] for y in range(4)),
                   lambda rows: (rows[y][2] for y in range(4)),
                   lambda rows: (rows[y][3] for y in range(4))])
#diag1
generators.append(lambda rows: (rows[0][0], rows[1][1], rows[2][2], rows[3][3]))
#diag2
generators.append(lambda rows: (rows[0][3], rows[1][2], rows[2][1], rows[3][0]))

with open('a.large') as fin:
    cases = int(fin.next())
    for testNo in range(1, cases + 1):
        rows       = [fin.next()[:-1] for i in range(4)]
        fin.next()

        output = "Draw"
        try:
            # check all possible lines...
            for gen in generators:
                if '.' not in gen(rows):
                    if 'X' not in gen(rows):
                        output = "O won"
                        raise Exception
                    if 'O' not in gen(rows):
                        output = "X won"
                        raise Exception
            
            if any('.' in row for row in rows):
                output = "Game has not completed"
        except Exception as e:
            pass

        print "Case #{0}: {1}".format(testNo, output)
