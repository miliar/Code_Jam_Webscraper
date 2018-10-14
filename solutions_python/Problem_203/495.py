def print_cake(data):
  for row in data:
    print ''.join(row)

def expand(data, char, i, j, rows, cols):
  min_x = j
  max_x = j+1
  # Expand left
  for idx, c in reversed(list(enumerate(data[i][0 : j]))):
    if c == '?':
      data[i][idx] = char
      min_x -= 1
    else:
      break

  # Expand right
  for idx, c in enumerate(data[i][j + 1 :]):
    if c == '?':
      data[i][idx + j + 1] = char
      max_x += 1
    else:
      break

  # Expand up
  for k in reversed(list(xrange(0, i))):
    if all(['?' == c for c in data[k][min_x : max_x]]):
      data[k][min_x : max_x] = [char for _ in xrange(min_x, max_x)]
    else:
      break

  # Expand down
  for k in xrange(i+1, rows):
    if all(['?' == c for c in data[k][min_x : max_x]]):
      data[k][min_x : max_x] = [char for _ in xrange(min_x, max_x)]
    else:
      break

  return data

def solve(data, rows, cols):
  visited = set()
  for i in range(rows):
    for j in range(cols):
      char = data[i][j]
      if char not in visited and char != '?':
        visited.add(char)
        data = expand(data, char, i, j, rows, cols)
  return data

if __name__ == '__main__':

  num_cases = int(raw_input())
  for case in range(num_cases):
    line = raw_input().split(' ')
    rows, cols = int(line[0]), int(line[1])
    data = []
    for _ in range(rows):
      data.append([c for c in raw_input().strip()])
    new_data = solve(data, rows, cols)

    print 'Case #{}:'.format(case+1)
    print_cake(data)
