def divisivel_por_3(numero):
  num_em_str = str(numero)
  soma = 0
  for digito in num_em_str:
    soma += int(digito)
  
  return soma % 3 == 0
  
def centro_inteiro(ponto1, ponto2, ponto3):
  soma_x = ponto1[0] + ponto2[0] + ponto3[0]
  if (not divisivel_por_3(soma_x)):
    return False
  else:
    soma_y = ponto1[1] + ponto2[1] + ponto3[1]
    if (not divisivel_por_3(soma_y)):
      return False
    else:
      return True

    
N = int(raw_input())
case_number = 1

for i in xrange(N):
  n, A, B, C, D, x0, y0, M = map(int, raw_input().split())
  pontos = []
  contagem = 0
  X = x0
  Y = y0
  pontos.append((X, Y))
  for i in xrange(n-1):
    X = (A * X + B) % M
    Y = (C * Y + D) % M
    pontos.append((X,Y))
  
  tam = len(pontos)
  #print tam
  
  for i in xrange(tam):
    for j in xrange(i+1, tam):
      for k in xrange(j+1, tam):
        if centro_inteiro(pontos[i], pontos[j], pontos[k]):
          contagem += 1
  
  print "Case #%d: %d" % (case_number, contagem)
  case_number +=1