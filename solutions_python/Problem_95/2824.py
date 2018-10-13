import sys,re,os

arq=open(sys.argv[1]).read()
linhas=arq.split('\n')
total=linhas[0]
nvalores=""
arq=open(sys.argv[1][:-4]+'.out','w')
for i in range(1,(int(total))+1):
	for x in range (len(linhas[i])):		
		if(linhas[i][x] == 'a'):
			nvalores = nvalores + "y"
		if(linhas[i][x] == 'b'):
			nvalores = nvalores +  "h"
		if(linhas[i][x] == 'c'):
			nvalores = nvalores +  "e"
		if(linhas[i][x] == 'd'):
			nvalores = nvalores +  "s"
		if(linhas[i][x] == 'e'):
			nvalores = nvalores +  "o"
		if(linhas[i][x] == 'f'):
			nvalores = nvalores +  "c"
		if(linhas[i][x] == 'g'):
			nvalores = nvalores +  "v"
		if(linhas[i][x] == 'h'):
			nvalores = nvalores +  "x"
		if(linhas[i][x] == 'i'):
			nvalores = nvalores +  "d"
		if(linhas[i][x] == 'j'):
			nvalores = nvalores +  "u"
		if(linhas[i][x] == 'k'):
			nvalores = nvalores +  "i"
		if(linhas[i][x] == 'l'):
			nvalores = nvalores +  "g"
		if(linhas[i][x] == 'm'):
			nvalores = nvalores +  "l"
		if(linhas[i][x] == 'n'):
			nvalores = nvalores +  "b"
		if(linhas[i][x] == 'o'):
			nvalores = nvalores +  "k"
		if(linhas[i][x] == 'p'):
			nvalores = nvalores +  "r"
		if(linhas[i][x] == 'q'):
			nvalores = nvalores +  "z"
		if(linhas[i][x] == 'r'):
			nvalores = nvalores +  "t"
		if(linhas[i][x] == 's'):
			nvalores = nvalores +  "n"
		if(linhas[i][x] == 't'):
			nvalores = nvalores +  "w"
		if(linhas[i][x] == 'u'):
			nvalores = nvalores +  "j"
		if(linhas[i][x] == 'v'):
			nvalores = nvalores +  "p"
		if(linhas[i][x] == 'w'):
			nvalores = nvalores +  "f"
		if(linhas[i][x] == 'x'):
			nvalores = nvalores +  "m"
		if(linhas[i][x] == 'y'):
			nvalores = nvalores +  "a"
		if(linhas[i][x] == 'z'):
			nvalores = nvalores +  "q"
		if(linhas[i][x] == ' '):
			nvalores = nvalores +  " "
		if(linhas[i][x] == '\n'):
			nvalores = nvalores +  "\n"

			
	arq.write("Case #"+str(i)+": "+nvalores+'\n')
	nvalores = ''
		


arq.close()

