inputfile = "A-large.in"
outputfile = inputfile + ".output"
input = open(inputfile).read()
output = open(outputfile, "w")

def evaluateGame(game):
  complete = False
  if (game.find(".") == -1):
    complete = True
  game = game.split("\n")
  game.append(game[0][0] + game[1][1] + game[2][2] + game[3][3])
  game.append(game[0][3] + game[1][2] + game[2][1] + game[3][0])
  
  game.append(game[0][0] + game[1][0] + game[2][0] + game[3][0])
  game.append(game[0][1] + game[1][1] + game[2][1] + game[3][1])
  game.append(game[0][2] + game[1][2] + game[2][2] + game[3][2])
  game.append(game[0][3] + game[1][3] + game[2][3] + game[3][3])
  for line in game:
    if (line.find(".") == -1 and line.find("X") == -1):
      return ("O won")
    elif (line.find(".") == -1 and line.find("O") == -1):
      return ("X won")
  if (complete):
    return "Draw"
  else:
    return "Game has not completed"

cases = int(input.split("\n")[0])
games = input.split("\n")[1:]
for i in range(cases):
  outputline = "Case #" + str(i + 1) + ": " + evaluateGame("\n".join(games[5 * i:5 * i + 4])) + "\n"
  output.write(outputline)
output.close()
