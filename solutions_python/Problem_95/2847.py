table = [
  [ ' ', ' ' ],
  [ 'a', 'y' ],
  [ 'b', 'h' ],
  [ 'c', 'e' ],
  [ 'd', 's' ],
  [ 'e', 'o' ],
  [ 'f', 'c' ],
  [ 'g', 'v' ],
  [ 'h', 'x' ],
  [ 'i', 'd' ],
  [ 'j', 'u' ],
  [ 'k', 'i' ],
  [ 'l', 'g' ],
  [ 'm', 'l' ],
  [ 'n', 'b' ],
  [ 'o', 'k' ],
  [ 'p', 'r' ],
  [ 'q', 'z' ],
  [ 'r', 't' ],
  [ 's', 'n' ],
  [ 't', 'w' ],
  [ 'u', 'j' ],
  [ 'v', 'p' ],
  [ 'w', 'f' ],
  [ 'x', 'm' ],
  [ 'y', 'a' ],
  [ 'z', 'q' ],
]
fin = open('A-small-attempt0.in', 'r')
case = 0
for line in fin:
  if case == 0:
    case += 1
    continue
  out = 'Case #' + str(case) + ": "
  for ch in line[:-1]:
    for r in range(len(table)):
      if ch == table[r][0]:
        out += table[r][1]
  print out,
  print ""
  case += 1
fin.close()
