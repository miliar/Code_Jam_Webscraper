cases = int(raw_input())
for case in range(cases):
  n, k = map(int, raw_input().split())
  board = []
  found = {"B": False, "R": False}

  for i in range(n):
    board.append(list(raw_input().strip()))

  for row in board:
    for i in range(n):
      if all([x == "." for x in row[:-1 - i]]):
        break

      while row[-1 - i] == ".":
        row.insert(0, ".")
        del row[-1 - i]

#  for row in board:
#    print "".join(row)

  for row in range(n):
    for col in range(n):
      target = board[row][col]

      if target == "." or found[target]:
        continue

      deltas = [[0, 1], [1, 0], [-1, 1], [1, 1]]
      for d in deltas:
        dx, dy = d
        cont = 1

        try:
          while cont < k and board[row + dy][col + dx] == target:
            cont += 1
            dx += d[0]
            dy += d[1]
        except IndexError:
          continue

        if cont == k:
          found[target] = True

  if found["B"] and found["R"]:
    result = "Both"
  elif found["B"]:
    result = "Blue"
  elif found["R"]:
    result = "Red"
  else:
    result = "Neither"

  print "Case #%d: %s" % (case + 1, result)
