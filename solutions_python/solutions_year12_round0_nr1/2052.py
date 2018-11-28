from string import maketrans

arq = open('speakresult.txt' , 'w')
t , i = int(raw_input()) , 1

while t != 0 :
	stin = 'ynficwlbkuomxsevzpdrjgthaq'
	stout = 'abcdefghijklmnopqrstuvwxyz'
	sttrans = maketrans(stin , stout)
	string = str(raw_input())

	arq.write('Case #%d: ' %(t - (t - i)) + string.translate(sttrans) + '\n')

	t , i = t - 1 , i + 1
