from os import system
import sys
sys.stdout = open("A-small-output.txt", "w")

f = open("A-small-attempt0.in", "r")
input = f.read().strip()

input = input.split('\n\n')

# FORMAT INPUT
formattedInput = []
for game in input:
	formattedInput += [game.split('\n')]
del formattedInput[0][0]

# OUTPUTS
winstr = ['Game has not completed','X won','O won','Draw']
for key,game in enumerate(formattedInput):
	win = i = 0
	if (game[0] or game[1] or game [2] or game[3]) in ('XXXX','TXXX','XTXX','XXTX','XXXT'):
		win = 1
	elif (game[0] or game[1] or game [2] or game[3]) in ('OOOO','TOOO','OTOO','OOTO','OOOT'):
		win = 2
	elif (game[0][0] + game[1][1] + game [2][2] + game[3][3]) in ('XXXX','TXXX','XTXX','XXTX','XXXT'):
		win = 1
	elif (game[0][0] + game[1][1] + game [2][2] + game[3][3]) in ('OOOO','TOOO','OTOO','OOTO','OOOT'):
		win = 2
	elif (game[0][3] + game[1][2] + game [2][1] + game[3][0]) in ('XXXX','TXXX','XTXX','XXTX','XXXT'):
		win = 1
	elif (game[0][3] + game[1][2] + game [2][1] + game[3][0]) in ('OOOO','TOOO','OTOO','OOTO','OOOT'):
		win = 2
	while win == 0 and i <= 3:		
		if (game[0][i] + game[1][i] + game [2][i] + game[3][i]) in ('XXXX','TXXX','XTXX','XXTX','XXXT'):
			win = 1
		elif (game[0][i] + game[1][i] + game [2][i] + game[3][i]) in ('OOOO','TOOO','OTOO','OOTO','OOOT'):
			win = 2
		i+=1
	if win == 0 and (game[0].find('.') or game[1].find('.') or game[2].find('.') or game[3].find('.')) == -1:
		win = 3
	print("Case #"+str(key+1)+": "+winstr[win])

system("pause")