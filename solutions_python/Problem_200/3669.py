n = int(input())  # read a line with a single integer

for i in range(1, n + 1):
  m = input()
  cont = True

  while cont:
      cont = False
      mlist = list(m)
      min = 0
      for j, ch in enumerate(mlist):
        chiffre = int(ch)
        if chiffre < min:
            mlist[j-1] = str(int(mlist[j-1])-1)
            for k in range(j, len(mlist)):
                mlist[k] = '9'
            cont = True
            continue
        else:
            min = chiffre
      mint = int(''.join(mlist))
      m = str(mint)

  print("Case #" + str(i) + ": " + m)