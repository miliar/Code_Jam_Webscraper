import sys

name = sys.argv[1]

with open(name) as f:
    lignes, colonnes, diagonales, out = list(), list(), list(), str()
    index = 1
    for line in f.readlines()[1:]:
        line = line[:-1] if line[-1] == '\n' else line
        if len(lignes) == 4:
            for i in range(4):
                col = str()
                for ligne in lignes:
                    col = col + ligne[i]
                colonnes.append(col)
            
            diag1, diag2 = str(), str()
            for i in range(4):
                diag1 = diag1 + lignes[i][i]
                diag2 = diag2 + lignes[i][-(i+1)]
            diagonales.extend([diag1, diag2])
            
            # print lignes
            # print colonnes
            # print diagonales
            def check(fours):
                not_finished = False
                for four in fours:
                    if four.count('.'):
                        not_finished = True
                        continue
                    for player in ['X', 'O']:
                        if four.count(player) == 4 or (four.count('T') and four.count(player) == 3):
                            return "%s won" % player
                if not_finished:
                    return "Game has not completed"
                return "Draw"
                        
            out = check(lignes + colonnes + diagonales)
                    
                
            print "Case #%d: %s" % (index, out)
            lignes, colonnes, diagonales, out = list(), list(), list(), str()
            index += 1
        else:
            lignes.append(line)
