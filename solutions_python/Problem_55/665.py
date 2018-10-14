import sys

lista_casos = []
resultados  = []

# Abre o arquivo para leitura e para gravacao
arquivo_entrada = open('./C-small.in', 'r')
arquivo_saida   = open('./C-small.out', 'w')

# Le o numero de casos
casos = arquivo_entrada.readline()

# Checa se a linha nao existe
if casos == '':
  arquivo_saida.write('Incorrect input file, no test cases number.\n')
  sys.exit()

casos = int(casos)

# Checa se o numero de casos nao ultrapassa o limite
if casos < 1 or casos > 50:
  arquivo_saida.write('Number of cases incorrect.\n')
  sys.exit()

# Le os casos e adiciona na lista de casos
i = 0
while i < casos:
  linha = arquivo_entrada.readline()
  
  # Checa se a linha nao existe
  if linha == '':
    arquivo_saida.write('Incorrect input file, number of test cases doesn\'t \
                        match')
    sys.exit()
  
  linha = linha.split()
  
  # Checa se a linha possui os tres parametros necessarios
  try:
    num_voltas  = int(linha[0])
    num_pessoas = int(linha[1])
    num_grupos  = int(linha[2])
  except IndexError:
    arquivo_saida.write('Incorrect case number ' + str(i + 1) + '.\n')
    sys.exit()
  
  # Checa a integridade dos parametros
  if num_voltas < 1 or num_voltas > 1000 or num_pessoas < 1 or \
     num_pessoas > 100 or num_grupos < 1 or num_grupos > 10:
    arquivo_saida.write('Incorrect case number ' + str(i + 1) + '.\n')
    sys.exit()
  
  # Le os grupos do caso
  linha = arquivo_entrada.readline()
  
  # Checa se a linha nao existe
  if linha == '':
    arquivo_saida.write('Incorrect input file, line of groups for case ' + \
                        str(i + 1) + ' doesn\'t exists.\n')
    sys.exit()
  
  linha = linha.split()
  
  # Checa se o numero de grupos bate com os parametros da linha
  if len(linha) != num_grupos:
    arquivo_saida.write('The number of groups doesn\'t match in case ' + \
                        str(i + 1) + '.\n')
    sys.exit()
  
  # Adiciona caso a lista de casos
  lista_casos.append([])
  lista_casos[i].append(num_voltas)
  lista_casos[i].append(num_pessoas)
  lista_casos[i].append([])
  for grupo in linha:
    grupo = int(grupo)
    
    # Checa se o numero de pessoas no grupo e valido e menor q a capacidade
    if grupo < 1 or grupo > 10 or grupo > num_pessoas:
      arquivo_saida.write('Number of people in the group not valid under case \
                          number ' + str(i + 1) + '.\n')
      sys.exit()
    
    lista_casos[i][2].append(grupo)
  
  i += 1

# Trata cada caso
i = 0
while i < casos:
  dinheiro = 0
  fila     = lista_casos[i][2]
  
  # Trata cada volta da montanha russa
  j = 0
  while j < lista_casos[i][0]:
    volta    = 0
    montanha = []
    
    # Trata a fila
    while volta <= lista_casos[i][1]:
      # Se o proximo grupo da fila nao exceder o numero de pessoas
      if len(fila) > 0 and (volta + fila[0]) <= lista_casos[i][1]:
        volta    += fila[0]
        dinheiro += fila[0]
        montanha.append(fila[0])
        del fila[0]
      else:
        fila.extend(montanha)
        break;
    
    j += 1
  
  # Adiciona resultado a lista de resultados
  resultados.append(dinheiro)
  
  i += 1

# Gera o arquivo de saida
i = 0
while i < casos:
  arquivo_saida.write('Case #' + str(i + 1) + ': ' + str(resultados[i]) + '\n')
  
  i += 1
