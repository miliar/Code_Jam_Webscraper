#!/usr/bin/python

import sys
	
if 1==1:#sys.stdin.readline().rstrip("\n")=='Input':
	count = int(sys.stdin.readline(),10)
	for i in range(0,count):
		line1=sys.stdin.readline().rstrip("\n")
		line2=sys.stdin.readline().rstrip("\n")
		line3=sys.stdin.readline().rstrip("\n")
		line4=sys.stdin.readline().rstrip("\n")
		temp=sys.stdin.readline().rstrip("\n")
		res="Draw"
		end=0

# X Won
		if (line1[0]=='X' or line1[0]=='T') and (line1[1]=='X' or line1[1]=='T') and (line1[2]=='X' or line1[2]=='T') and (line1[3]=='X' or line1[3]=='T'):
			res="X won"
			end=1
		if (line2[0]=='X' or line2[0]=='T') and (line2[1]=='X' or line2[1]=='T') and (line2[2]=='X' or line2[2]=='T') and (line2[3]=='X' or line2[3]=='T'):
			res="X won"
			end=1
		if (line3[0]=='X' or line3[0]=='T') and (line3[1]=='X' or line3[1]=='T') and (line3[2]=='X' or line3[2]=='T') and (line3[3]=='X' or line3[3]=='T'):
			res="X won"
			end=1
		if (line4[0]=='X' or line4[0]=='T') and (line4[1]=='X' or line4[1]=='T') and (line4[2]=='X' or line4[2]=='T') and (line4[3]=='X' or line4[3]=='T'):
			res="X won"
			end=1
		if (line1[0]=='X' or line1[0]=='T') and (line2[1]=='X' or line2[1]=='T') and (line3[2]=='X' or line3[2]=='T') and (line4[3]=='X' or line4[3]=='T'):
			res="X won"
			end=1
		if (line4[0]=='X' or line4[0]=='T') and (line3[1]=='X' or line3[1]=='T') and (line2[2]=='X' or line2[2]=='T') and (line1[3]=='X' or line1[3]=='T'):
			res="X won"
			end=1

		if (line1[0]=='X' or line1[0]=='T') and (line2[0]=='X' or line2[0]=='T') and (line3[0]=='X' or line3[0]=='T') and (line4[0]=='X' or line4[0]=='T'):
			res="X won"
			end=1

		if (line1[1]=='X' or line1[1]=='T') and (line2[1]=='X' or line2[1]=='T') and (line3[1]=='X' or line3[1]=='T') and (line4[1]=='X' or line4[1]=='T'):
			res="X won"
			end=1

		if (line1[2]=='X' or line1[2]=='T') and (line2[2]=='X' or line2[2]=='T') and (line3[2]=='X' or line3[2]=='T') and (line4[2]=='X' or line4[2]=='T'):
			res="X won"
			end=1

		if (line1[3]=='X' or line1[3]=='T') and (line2[3]=='X' or line2[3]=='T') and (line3[3]=='X' or line3[3]=='T') and (line4[3]=='X' or line4[3]=='T'):
			res="X won"
			end=1

# O Won

		if (line1[0]=='O' or line1[0]=='T') and (line1[1]=='O' or line1[1]=='T') and (line1[2]=='O' or line1[2]=='T') and (line1[3]=='O' or line1[3]=='T'):
			res="O won"
			end=1
		if (line2[0]=='O' or line2[0]=='T') and (line2[1]=='O' or line2[1]=='T') and (line2[2]=='O' or line2[2]=='T') and (line2[3]=='O' or line2[3]=='T'):
			res="O won"
			end=1
		if (line3[0]=='O' or line3[0]=='T') and (line3[1]=='O' or line3[1]=='T') and (line3[2]=='O' or line3[2]=='T') and (line3[3]=='O' or line3[3]=='T'):
			res="O won"
			end=1
		if (line4[0]=='O' or line4[0]=='T') and (line4[1]=='O' or line4[1]=='T') and (line4[2]=='O' or line4[2]=='T') and (line4[3]=='O' or line4[3]=='T'):
			res="O won"
			end=1
		if (line1[0]=='O' or line1[0]=='T') and (line2[1]=='O' or line2[1]=='T') and (line3[2]=='O' or line3[2]=='T') and (line4[3]=='O' or line4[3]=='T'):
			res="O won"
			end=1
		if (line4[0]=='O' or line4[0]=='T') and (line3[1]=='O' or line3[1]=='T') and (line2[2]=='O' or line2[2]=='T') and (line1[3]=='O' or line1[3]=='T'):
			res="O won"
			end=1

		if (line1[0]=='O' or line1[0]=='T') and (line2[0]=='O' or line2[0]=='T') and (line3[0]=='O' or line3[0]=='T') and (line4[0]=='O' or line4[0]=='T'):
			res="O won"
			end=1

		if (line1[1]=='O' or line1[1]=='T') and (line2[1]=='O' or line2[1]=='T') and (line3[1]=='O' or line3[1]=='T') and (line4[1]=='O' or line4[1]=='T'):
			res="O won"
			end=1

		if (line1[2]=='O' or line1[2]=='T') and (line2[2]=='O' or line2[2]=='T') and (line3[2]=='O' or line3[2]=='T') and (line4[2]=='O' or line4[2]=='T'):
			res="O won"
			end=1

		if (line1[3]=='O' or line1[3]=='T') and (line2[3]=='O' or line2[3]=='T') and (line3[3]=='O' or line3[3]=='T') and (line4[3]=='O' or line4[3]=='T'):
			res="O won"
			end=1

		if end==0 and (line1[0]=='.' or line2[0]=='.' or line3[0]=='.' or line4[0]=='.' or line1[1]=='.' or line2[1]=='.' or line3[1]=='.' or line4[1]=='.' or line1[2]=='.' or line2[2]=='.' or line3[2]=='.' or line4[2]=='.' or line1[3]=='.' or line2[3]=='.' or line3[3]=='.' or line4[3]=='.'):
			res="Game has not completed"

		print("Case #"+str(i+1)+": "+res)
		

	
#End
