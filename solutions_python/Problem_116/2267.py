
import sys

def debug(str):
    #print str
    pass

def all_same(markers):
    team = ""
    for m in markers:
        if m == '.':
            return (False, " ")
        if m == 'T':
            continue
        elif team == "":
            team = m
            continue

        if m != team:
            return (False, " ")
    return (True, team)

def winner(rows):
    
    ''' 4 strings each 4 chars wide '''

    #cols
    trans = []
    for i in range(4):
        col = ""
        for j in range(4):
            col = col + rows[j][i]
        trans.append(col)
    for col in trans:
        debug( "testing col  %s" % col)
        (res, team) = all_same(col)
        if res:
            return "%s won" % team 

    #rows
    for row in rows:
        debug( "testing row %s" % row)
        (res, team) = all_same(row)
        if res:
            return "%s won" % team

    # dig
    markers = ""
    for i in range(4):
        markers += rows[i][i]
         
    debug( "testing diag 1 %s" % markers )
    (res, team) = all_same(markers)
    if res:
        return "%s won" % team

    i = 0
    j = 3
    markers = ""
    for x in range(4):
        markers += rows[i][j]
        j = j - 1
        i = i + 1
    debug( "testing diag 2 %s" % markers)
    (res, team) = all_same(markers)
    if res:
        return "%s won" % team

    # no winner
    for row in rows:
        for char in row:
            if char == '.':
                res = "Game has not completed"
                return res
    
    return "Draw"
    
game0 = ["1001", 
         "1000",     
         "0100",
         "0010"]

game1 = ["T001", 
         "1000",     
         "0100",
         "0010"]

game2 = ["0001", 
         "1000",     
         "0100",
         "001T"]

game3 = ["0001", 
         "1000",     
         "0100",
         "001."]
        
game4 = ["..01", 
         "1000",     
         "0100",
         "001."]

game5 = ["0001", 
         "1000",     
         "0100",
         "00T."]

game6 = ["0001", 
         "1000",     
         "0100",
         "0011"]

game7 = ["1111", 
         "1000",     
         "0100",
         "0011"]

game8 = ["111T", 
         "1000",     
         "0100",
         "0010"]

def test():
    games = []
    games.append((game0, "Draw"))
    games.append((game1, "0 won"))
    games.append((game2, "0 won"))
    games.append((game3, "Game has not completed"))
    games.append((game4, "Game has not completed"))
    games.append((game5, "0 won"))
    games.append((game6, "Draw"))
    games.append((game7, "1 won"))
    games.append((game8, "0 won"))

    for game in games:


        debug( "game %s" % str(game[0]))
        res = winner(game[0])
        if res == game[1]:
            print "passed"
        else:
            print "expected %s got %s" % (game[1], res)
            print game

#test()

def runner(input_file):
    lines = []
    with open(input_file, 'r') as f:
        lines = f.readlines()
    
    index = 0
    num_tests = int(lines[index].strip())
    index += 1

    for test in range(num_tests):
        # skip empty lines
        while lines[index].strip() == "":
            index += 1
        game = []
        for i in range(4):
            game.append(lines[index].strip())
            index += 1
        #print game 
        result = winner(game)
        print "Case #%d: %s" % (test + 1, result)


runner(sys.argv[1])



    
