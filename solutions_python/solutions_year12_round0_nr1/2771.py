string1 = 'our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up a o z q'
string2 = 'ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv y e q z'
string1=string1.split()
string2=string2.split()
mapa = {}
conta=int(raw_input())
case = 1
for i in range(len(string1)):
	for j in range(len(string1[i])):
		if string1[i][j] != ' ':
			mapa[string2[i][j]] = string1[i][j]

for v in range(conta):
	frase = list(raw_input())
	for i in range(len(frase)):
		if frase[i] != ' ':
			frase[i] = mapa[frase[i]]
	frase= "".join(frase)
	print "Case #"+str(case)+":",frase
	case+=1
