
entrada = file('A-large.in')
salida = file('output-large.ou', 'w')

casos = int(entrada.readline())

def aPerfecto(figura):
	for i in range(len(figura)):
		for j in range(len(figura[i])):
			if figura[i][j] == '#':
				figura[i][j] = '/'
				if i+1 < len(figura) and figura[i+1][j] == '#':
						figura[i+1][j] = '\\'
						if j+1 < len(figura[i]) and figura[i][j+1] == '#':
								figura[i][j+1] = '\\'
								if figura[i+1][j+1] == '#':
									figura[i+1][j+1] = '/'
								else:
									return False, 'Impossible'
						else:
							return False, 'Impossible'
				else:
					return False, 'Impossible'
	return True, figura
	

for w in range(casos):
	temp = entrada.readline().split()
	
	rows = int(temp[0])
	cols = int(temp[1])
	
	figura = []
	
	for i in range(rows):
		figura.append(list(entrada.readline()))
	
	sePuede, aux = aPerfecto(figura)
	
	if not sePuede:
		salida.write('Case #%d:\n%s\n' % ((w+1), str(aux)))
	else:
		salida.write('Case #%d:\n' % (w+1))
		for i in aux:
			for j in i:
				salida.write('%s' % j)
			salida.write('')
