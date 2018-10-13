example_lawns = """3
3 3
2 1 2
1 1 1
2 1 2
5 5
2 2 2 2 2
2 1 1 1 2
2 1 2 1 2
2 1 1 1 2
2 2 2 2 2
1 3
1 2 1""".split('\n')

def read_lawns(lines):
  num_lawns = int(lines[0])
  lines = lines[1:]
  for lawn in range(num_lawns):
    num_rows, _ = map(int, lines[0].strip().split())
    yield map(lambda line: map(int, line.strip().split()), lines[1:num_rows + 1])
    lines = lines[num_rows + 1:]

def num_rows(lawn):
  return len(lawn)

def num_cols(lawn):
  return len(lawn[0])

def get_height(lawn, x, y):
  return lawn[y][x]

def viable_row(lawn, x, y):
  height = get_height(lawn, x, y)
  return all(map(lambda nx: get_height(lawn, nx, y) <= height,
                 range(num_cols(lawn))))

def viable_column(lawn, x, y):
  height = get_height(lawn, x, y)
  return all(map(lambda ny: get_height(lawn, x, ny) <= height,
                 range(num_rows(lawn))))


def viable(lawn):
  for y in range(len(lawn)):
    for x in range(len(lawn[0])):
      if not (viable_column(lawn, x, y) or viable_row(lawn, x, y)):
        return False
  return True

# ran from python repl with
# import lawn
# lawn.main('lawn_file')
def main(filename):
  with open(filename, 'r') as inf:
    lawns = read_lawns(inf.readlines())
  with open(filename + '.out', 'w') as outf:
    counter = 1
    for lawn in lawns:
      print >> outf, "Case #%d: %s" % (counter, 'YES' if viable(lawn) else 'NO')
      counter += 1
