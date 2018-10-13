input_file = open("input.txt", "r")
output_file = open("output.txt", "w")
lines = input_file.readlines()

problems = []
problem = []

i = 0
for line in lines[1:]:
    if line == '\n': 
        continue

    problem.append(list(line[:-1]))
    i+=1

    if i == 4:
        i = 0
        problems.append(problem)
        problem = []

xCh, oCh, xCv, oCv, xD1, oD1, xD2, oD2, points = 0,0,0,0,0,0,0,0, 0

for p,problem in enumerate(problems):

    winner = None
    xD1, oD1, xD2, oD2, points = 0,0,0,0,0
        
    for i, row in enumerate(problem):

        for a, hCell in enumerate(row):
            vCell = problem[a][i]
            diagonal = (a == i)
            diagonal2 = (a == 0 and i == 3) or (a == 3 and i == 0) or (a == 1 and i == 2) or (i == 1 and a == 2)

            if hCell == 'X':
                xCh += 1
            elif hCell == 'O':
                oCh += 1
            elif hCell == 'T':
                xCh += 1
                oCh += 1
            else:
                points += 1

            if vCell == 'X':
                xCv += 1
                xD1 += 1 if diagonal else 0
                xD2 += 1 if diagonal2 else 0
            elif vCell == 'O':
                oCv += 1
                oD1 += 1 if diagonal else 0
                oD2 += 1 if diagonal2 else 0
            elif vCell == 'T':
                xCv += 1
                oCv += 1
                oD1 += 1 if diagonal else 0
                xD1 += 1 if diagonal else 0
                xD2 += 1 if diagonal2 else 0
                oD2 += 1 if diagonal2 else 0

        if xCh >= 4 or xCv >= 4 or xD1 >= 4 or xD2 >= 4:
            winner = "X won"
        elif oCh >= 4 or oCv >= 4 or oD1 >= 4 or oD2 >= 4: 
            winner = "O won"

        xCh, oCh, xCv, oCv = 0,0,0,0

    if winner is None:
        winner = "Draw" if points == 0 else "Game has not completed"

    output_file.write("Case #" + str(p+1) + ": " + winner + "\n")

output_file.close()