
arq = open("A-large.in","r")
out = open("amiltonLarge.out", "w")
T = int(arq.readline())

for i in range(T):
	#Executa loop:
	caso = arq.readline().split(" ")
	num_botoes = int(caso[0])
	botoes_orange = []
	botoes_blue = []
	vez_atual = []
	pos_orange = 1	
	pos_blue = 1
	tempo = 0
	botao_atual = 0
	botao_blue_atual = 0
	botao_orange_atual = 0
	acabou_blue = True
	acabou_orange = True
    
	for j in range(num_botoes):
		if caso[(2*j+1)] == "O":
			botoes_orange.append(int(caso[(2*j+2)]))
			acabou_orange = False
		else:
			botoes_blue.append(int(caso[(2*j+2)]))
			acabou_blue = False
		vez_atual.append(caso[(2*j+1)])
    
	while botao_atual < num_botoes:
		mudou = False
		if not acabou_blue:
			if pos_blue < botoes_blue[botao_blue_atual]:
				pos_blue += 1
			elif pos_blue > botoes_blue[botao_blue_atual]:
				pos_blue -= 1
			else:
				if vez_atual[botao_atual] == "B":
					botao_atual += 1
					mudou = True
					botao_blue_atual += 1
					if (botao_blue_atual == len(botoes_blue)):
						acabou_blue = True
		if not acabou_orange:
			if pos_orange < botoes_orange[botao_orange_atual]:
				pos_orange += 1
			elif pos_orange > botoes_orange[botao_orange_atual]:
				pos_orange -= 1
			else:
				if not mudou and vez_atual[botao_atual] == "O":
					botao_atual += 1
					botao_orange_atual += 1
					if botao_orange_atual == len(botoes_orange):
						acabou_orange = True
		tempo += 1
	out.write("Case #%i: %i\n" % ((i+1), tempo))
