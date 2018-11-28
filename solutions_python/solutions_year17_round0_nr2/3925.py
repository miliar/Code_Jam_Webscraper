print("Tidy Numbers")

f = open('input.in', 'r')
output = open('output.out', 'w')
lignes=iter(f.read().splitlines())
nbTests=int(next(lignes))

def tidy(nombre):
    chiffres = list(str(nombre))
    ancienChiffre = chiffres.pop(0)
    for unIndex,unChiffre in enumerate(chiffres):
        if unChiffre < ancienChiffre:
            return unIndex
        ancienChiffre = unChiffre
    return True

def transformer(nombre,index):
  chiffres = [int(x) for x in list(str(nombre))]
  if chiffres[index] > 0:
    chiffres[index] -= 1
  else:
    while chiffres[index] == 0:
      index -= 1
    chiffres[index] -= 1
  chiffres = [x if unIndex <= index else 9 for unIndex,x in enumerate(chiffres)]
  return int("".join([str(x) for x in chiffres]))

def lastTidy(nombre):
    isTidy = tidy(nombre)
    if type(isTidy) == type(True) and isTidy == True:
        return nombre
    nouveauNombre = transformer(nombre,isTidy)
    return lastTidy(nouveauNombre)

for numeroTest in range(0,nbTests):
    N = int(next(lignes))
    reponse = str(lastTidy(N))
    output.write("Case #"+str(numeroTest+1)+": "+reponse+"\n")
    print(reponse)