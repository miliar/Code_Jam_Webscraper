def ass(m, n):
  if m == 1:
    for i in xrange(0, n):
      yield [i]
  else:
    for i in xrange(0, n):
      for tail_ass in ass(m-1, n):
        yield [i] + tail_ass

debug = False

def count_nodes(m, n, words):
  # Assign the words in all the possible ways
  for word_ass in ass(m, n):
    servers = [{} for i in xrange(n)]
    for word_index in xrange(m):
      for prefix_length in xrange(len(words[word_index]) + 1):
        if debug:
          print "Add to server", word_ass[word_index], "string", words[word_index][:prefix_length]
        servers[word_ass[word_index]][words[word_index][:prefix_length]] = True
    # Count the number of nodes in this assignment
    count = 0
    for server in servers:
      count += len(server.keys())
    yield count

def solve(m, n, words):
  best = 0
  best_count = 0
  for result in count_nodes(m, n, words):
    if result == best:
      best_count += 1
    if result > best:
      best = result
      best_count = 1
  return (best, best_count)

def cl(m, n, words):
  return list(count_nodes(m, n, words))

def al(m, n):
  return list(ass(m, n))

for tc in xrange(int(raw_input())):
  mn = [int(i) for i in raw_input().split(" ")]
  words = []
  for i in xrange(mn[0]):
    words += [raw_input()]
  x, y = solve(mn[0], mn[1], words)
  print "Case #" + str(tc + 1) + ": " + str(x) + " " + str(y)
