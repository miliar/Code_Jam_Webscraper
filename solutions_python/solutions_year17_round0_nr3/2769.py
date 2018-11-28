print("Bathroom Stalls")

f = open('input.in', 'r')
output = open('output.out', 'w')
lignes=iter(f.read().splitlines())
nbTests=int(next(lignes))

for numeroTest in range(0,nbTests):
    N,K = [int(x) for x in next(lignes).split(" ")]
    pieces = [1] + [0 for i in range(0,N)] + [1]
    def rs(index):
      if pieces[index] == 1:
        return -1
      nb = 0
      index += 1
      while True:
        if pieces[index] == 1:
          break
        nb += 1
        index += 1
      return nb

    def ls(index):
      if pieces[index] == 1:
        return -1
      nb = 0
      index -= 1
      while True:
        if pieces[index] == 1:
          break
        nb += 1
        index -= 1
      return nb

    #Pour chaque entrant
    for k in range(0,K):
      tableau = []
      for index,piece in enumerate(pieces):
        droite = rs(index)
        gauche = ls(index)
        mini = min(droite,gauche)
        maxi = max(droite,gauche)
        tableau.append({"droite":droite,"gauche":gauche,"index":index,"mini":mini,"maxi":maxi})
      tableauTrie = sorted(tableau, key = lambda x: (-x["mini"], -x["maxi"],x["index"]))
      pieces[tableauTrie[0]["index"]] = 1
    reponse = " ".join([str(x) for x in [tableauTrie[0]["maxi"],tableauTrie[0]["mini"]]])
    output.write("Case #"+str(numeroTest+1)+": "+reponse+"\n")
    print(reponse)