import collections

def flip(pattern):
  return ''.join(map(lambda c: '-' if c == '+' else '+', pattern))

def get_neighbors(vertex, k):
  results = []
  for i in xrange(0, len(vertex) - k + 1):
    results.append(vertex[0 : i] + flip(vertex[i : i + k]) + vertex[i + k :])
  return results

def solve(pattern, k):
  visited, queue = set(pattern), collections.deque([(0, pattern)])
  solution = '+'*len(pattern)
  while queue:
    depth, vertex = queue.popleft()
    if vertex == solution:
      return depth
    for neighbour in get_neighbors(vertex, k):
      if neighbour not in visited:
        visited.add(neighbour)
        queue.append((depth + 1, neighbour))
  return 'IMPOSSIBLE'

if __name__ == '__main__':

  num_cases = int(raw_input())
  for case in range(num_cases):
    line = raw_input().split(' ')
    pattern = line[0]
    k = int(line[1])

    print 'Case #{}: {}'.format(case+1, solve(pattern, k))
