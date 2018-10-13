import sys

lista_casos   = []
resultados    = []
arquivo_saida = open('./A-large.out', 'w')

# Le o arquivo
arquivo = open('A-large.in', 'r')

# Pega a quantidade de casos
casos = int(arquivo.readline())

# Ve se o numero de casos esta correto
if casos < 1 or casos > 10000:
  print "Number of test cases invalid."
  sys.exit()

# Coloca os casos na lista
i = 0
while i < casos:
  # Le o caso
  linha = arquivo.readline()
  
  # Valida a linha
  if linha == '':
    print 'Number of cases don\'t match the real number of cases lines.'
    sys.exit()
  
  caso  = linha.split()
  
  # Valida o numero de argumentos do caso
  try:
    snappers = int(caso[0])
    snaps    = int(caso[1])
  except IndexError:
    print 'Invalid number of arguments on case ' + str(i + 1) + '.'
    sys.exit()
  
  # Valida o caso
  if snappers < 1 or snappers > 30 or snaps < 0 or snaps > (10**8):
    print 'Case ' + str(i + 1) + ' isn\'t a valid case.'
    sys.exit()
  
  # Adiciona o caso a lista de casos
  lista_casos.append({'snappers': snappers, 'snaps': snaps})
  
  i += 1

# Testa os casos
i = 0
while i < casos:
  # Transforma o numero de snaps em binario para verificar se o ultimo snapper
  # esta ligado
  snaps_bin = bin(lista_casos[i]['snaps'])
  
  # Verifica se o snapper esta ligado
  if snaps_bin[(len(snaps_bin) - lista_casos[i]['snappers']):] == \
     ('1' * lista_casos[i]['snappers']):
    resultados.append('ON')
  else:
    resultados.append('OFF')
  
  i += 1

# Imprime os resultados
i = 0
while i < casos:
  arquivo_saida.write('Case #' + str(i + 1) + ': ' + resultados[i] + \
                      '\n')
  
  i += 1

