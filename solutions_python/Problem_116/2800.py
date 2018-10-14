def iter_file_lines(filename):
  with open(filename) as f:
    for line in f:
      line = line.rstrip()
      if len(line):
        yield line

EMPTY = '.'
TOMEK = 'T'

def arrangement_itterator(rows):
  # rows first
  for row in rows:
    yield row

  # cols
  for i in range(4):
    yield tuple(row[i] for row in rows)

  # diagonal
  yield tuple(rows[i][i] for i in range(4))
  yield tuple(rows[i][3-i] for i in range(4))

def game_status(rows):
  empty_spots = False

  for arr in arrangement_itterator(rows):
    if EMPTY in arr:
      empty_spots = True
      continue

    unique = set(arr)
    unique.discard(TOMEK)
    if len(unique) == 1:
      return "%s won" % arr[0]

  if empty_spots:
    return "Game has not completed"

  return "Draw"

if __name__ == '__main__':
  lines = iter_file_lines('A-small-attempt0.in')
  testcases = int(lines.next())
  for i in range(testcases):
    rows = [tuple(lines.next()) for _ in range(4)]
    status = game_status(rows)
    print "Case #%i: %s" % (i + 1, status)
