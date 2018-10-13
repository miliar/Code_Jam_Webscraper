def chunker(seq, size):
    return (seq[pos:pos + size] for pos in xrange(0, len(seq), size))

def gamelist_builder(filename):
    with open(filename, 'rU') as f:
        f_contents = f.readlines()
    f.close()

    long_string = ""
    game_num = int(f_contents[0])
    for item in f_contents[1:]:
        long_string = long_string + item.rstrip()
    game_list = []
    for chunk in chunker(long_string, 16):
        chunklist = []
        for char in chunk:
            chunklist.append(char)
        game_list.append(chunklist)
    return (game_list, game_num)

game_list, num_games = gamelist_builder("A-large.in")

def win_check(game):

    X_wins = ['XXXT', 'XXTX', 'XTXX', 'TXXX', 'XXXX']
    O_wins = ['OOOT', 'OOTO', 'OTOO', 'TOOO', 'OOOO']

    #test down solutions
    
    for i in [0,1,2,3]:
        test_string = game[i] + game[i+4] + game[i+8] + game[i+12]
        if test_string in X_wins:
            return "X won"
        if test_string in O_wins:
            return "O won"

    #test right solutions
    for i in [0,4,8,12]:
        test_string = game[i] + game[i+1] + game[i+2] + game[i+3]
        if test_string in X_wins:
            return "X won"
        if test_string in O_wins:
            return "O won"

    #test down-right solutions
    test_string = game[0] + game[5] + game[10] + game[15]
    if test_string in X_wins:
        return "X won"
    if test_string in O_wins:
        return "O won"

    #test down-left solutions
    test_string = game[3] + game[6] + game[9] + game[12]
    if test_string in X_wins:
        return "X won"
    if test_string in O_wins:
        return "O won"

    if "." not in game:
        return "Draw"

    else:
        return "Game has not completed"




def output_compiler(game_list, num_games):
    outputlines = []
    for x in range(num_games):
        outcome = win_check(game_list[x])
        case_output = "Case #{0}: {1}\n".format(x+1, outcome)
        outputlines.append(case_output)
    


    f = open("tttt_output.txt", "w")
    f.writelines(outputlines)
    f.close()
        
        #outputlines.append("Case #{0}: {1}".format(x, outcome)
    #print outputlines

output_compiler(game_list, num_games)



    
   # for z in range(16):
    #   print int(next(all_games_string))
        
    



    
    
    
