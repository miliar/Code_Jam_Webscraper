import string
file = open("b.in","r")

t = int(file.readline().rstrip())

def solve(elem, trans, matrix):
  l = []
  len_elem = len(elem)
  idx = 0
  while idx < len_elem:
    e = elem[idx]

    if len(l) == 0:
      l.append(e)
    else:
      top = l[len(l)-1]
      (plm,plt) = sorted([e,top])
      if(trans[plm][plt] != 0):
        l.pop()
        l.append(trans[plm][plt])
      else:
        gasit = 0
        for miez in l:
          (plm,plt) = sorted([e,miez])
          if matrix[plm][plt] != 0:
            gasit = 1
            l = []
            break
        if gasit == 0:
          l.append(e)

    idx+= 1
  return l

def makeTrans():
  letters = string.uppercase
  t = {}
  for i in range(len(letters)):
    t[letters[i]] = {}
    for j in range(len(letters)):
      t[letters[i]][letters[j]] = 0
  return t

for abis in range(t):
  line = file.readline().rstrip().split(" ")
  C = int(line[0])

  nr = 1
  trans = makeTrans()
  magic = makeTrans()
  for i in range(C):
    elem = line[nr]
    idx = "".join(sorted(elem[0:2]))
    trans[idx[0]][idx[1]] = elem[2]
    nr+= 1

  D = int(line[nr])
  nr += 1
  matrix = makeTrans()
  for i in range(D):
    elem = line[nr]
    idx = "".join(sorted(elem[0:2]))
    matrix[idx[0]][idx[1]] = 1
    nr+= 1

  nr += 1
  elem = line[nr]

  res = solve(elem,trans,matrix)
  out = "Case #"+str(abis+1)+": ["
  for i in range(len(res)):
    out += str(res[i])
    if(i != len(res)-1):
      out += ', '
  out += "]"
  print out
