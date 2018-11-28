def isTidy(liste):
  previous = 0
  count = 0
  for digit in liste:
    if int(digit) < previous:
      return count
    previous = int(digit)
    count += 1

  return -1


t = int(input())
for i in range(1, t+1):
  n = int(input())
  out = 1

  liste = []
  for digit in str(n):
    liste.append(int(digit))
  
  if isTidy(liste) == -1:
    out = n
  else:
    index = isTidy(liste)
    while index != -1:
      liste[index-1] -= 1
      for y in range(index, len(liste)):
        liste[y] = 9
      index = isTidy(liste)

    #transforms a list of int into 1 int
    out = int(''.join(map(str,liste)))

  print("Case #{}: {}".format(i, out))