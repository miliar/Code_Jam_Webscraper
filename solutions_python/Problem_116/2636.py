import string
import re
 


def seperate_game(remaining_games):
  
    game= remaining_games[0:4]
    return game
   
    
def grade_game_row(game, number):
    num = str(number)
    for row in game:
        
        if row == "XXXX" or row == "TXXX" or row == "XXXT" or row == "XXTX" or row == "XTXX":
            win = "Case #" + num + ": X won"
            return win
        if row == "OOOO" or row == "TOOO" or row == "OOOT" or row == "OOTO" or row == "OTOO":
            win2 = "Case #" + num + ": O won"
            return win2

    return None

    
def grade_game_col(game, number):
    num = str(number)
    all_e = []
    game_col = []
    for row in game:
        for e in row:
            all_e.append(e)
            
    game_col = [[all_e[0],all_e[4],all_e[8],all_e[12]],[all_e[1],all_e[5],all_e[9],all_e[13]]
           ,[all_e[2],all_e[6],all_e[10],all_e[14]],[all_e[3],all_e[7],all_e[11],all_e[15]]]
    for col in game_col:
        gradeablestring = ''
        newString = [gradeablestring.join(col)]
    
        if newString == ["XXXX"] or newString == ["TXXX"] or newString == ["XXXT"] or newString == ["XXTX"] or newString == ["XTXX"]:
            win = "Case #" + num + ": X won"
            return win
        if newString == ["OOOO"] or newString ==["TOOO"] or newString ==["OOOT"]or newString ==["OOTO"] or newString ==["OTOO"]:
            win2 = "Case #" + num + ": O won"
            return win2

    return None
def grade_game_diag(game, number):
    num = str(number)
    all_e = []
    game_diag = []
    for row in game:
        for e in row:
            all_e.append(e)
    game_diag = [[all_e[0],all_e[5],all_e[10],all_e[15]],[all_e[3],all_e[6],all_e[9],all_e[12]]]
    #print game_diag
    for diag in game_diag:
        gradeablestring = ''
        newString = [gradeablestring.join(diag)]
        
        if newString == ["XXXX"] or newString == ["TXXX"] or newString == ["XXXT"] or newString == ["XXTX"] or newString == ["XTXX"]:
            win = "Case #" + num + ": X won"
            return win
        if newString == ["OOOO"] or newString ==["TOOO"] or newString ==["OOOT"]or newString ==["OOTO"] or newString ==["OTOO"]:
            win2 = "Case #" + num + ": O won"
            return win2
def check_for_period(game):
    all_e = []
    for row in game:
        for e in row:
            all_e.append(e)
    if '.' in all_e:
        return True


fo = open("A-large-attempt.txt", "r")
data = fo.read()
all_games = data[4:]
num_of_games = 1000
all_rows = all_games.split("\n")
game_rows = [e for e in all_rows if len(e) != 0]



game_number = 0

while num_of_games > game_number:
    game_number += 1 
    num = str(game_number)
    game = seperate_game(game_rows)
   
    out1 =grade_game_col(game, game_number)
    out2 =grade_game_row(game, game_number)
    out3 = grade_game_diag(game, game_number)

    
        

    if out1 != None and out1 != out2 and out1!= out3:
       print out1
        
    if out2 != None and out2!= out3:
        print out2
        
    if out3 != None:
        print out3
        
    if out1 == None and out2 == None and out3 == None:
        if check_for_period(game):
            print "Case #" + num + ": Game has not completed"
        else:
            print "Case #" + num + ": Draw"

   

    game_rows = game_rows[4:]
    
