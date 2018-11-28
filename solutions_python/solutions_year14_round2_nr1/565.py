ttt = int(input())

for tti in range(ttt):
  print("Case #%d:" % (tti+1), end=" ")
  n = int(input())
  L = []
  W = []
  for i in range(n):
    a = input()
    L.append(a)
    W.append(0)
  X = []
  try:
  #if True:
    while True:
      czy = False
      for i in range(n):
        if W[i] < len(L[i]):
          czy = True
      if(czy == False):
        break
      Y = []
      litera = L[0][W[0]]
      for i in range(n):
        tmp = 0
        while W[i]<len(L[i]) and litera==L[i][W[i]]:
          W[i] += 1
          tmp += 1
        if tmp == 0:
          tmp /= 0
        Y.append(tmp)
      X.append(Y)
    wynik = 0
    for linia in X:
      srednia = 0
      for wyraz in linia:
        srednia += wyraz
      srednia //= n
      for wyraz in linia:
        wynik += abs(wyraz-srednia)
    #print("")
    #print(L[0])
    #print(L[1])
    print(wynik)
  except:
    #print("")
    #print(L[0])
    #print(L[1])
    print("Fegla Won")  