import sys

def preProcess(n, h, graph):
  for k in range(n):
    for i in range(n):
      for j in range(n):
        if graph[i][k] == -1 or graph[k][j] == -1:
          continue
        nd = graph[i][k] + graph[k][j]
        if graph[i][j] == -1 or nd < graph[i][j]:
          graph[i][j] = nd

  matrix = []
  for i in range(n):
    v = [None] * n
    for j in range(n):
      if graph[i][j] == -1 or h[i][0] < graph[i][j]:
        continue
      v[j] = float(graph[i][j]) / h[i][1]
    matrix.append(v)

  for k in range(n):
    for i in range(n):
      for j in range(n):
        if matrix[i][k] == None or matrix[k][j] == None:
          continue
        nd = matrix[i][k] + matrix[k][j]
        if matrix[i][j] == None or nd < matrix[i][j]:
          matrix[i][j] = nd
  return matrix

if __name__ == "__main__":
  data = open(sys.argv[1]).readlines()
  t = int(data[0])
  idx = 1
  for i in range(1, t+1):
    [n, q] = [int(x) for x in data[idx].split(" ")]
    idx += 1
    h = []
    for j in range(n):
      [e, s] = [int(x) for x in data[idx].split(" ")]
      h.append([e, s])
      idx += 1

    graph = []
    for j in range(n):
      row = [int(x) for x in data[idx].split(" ")]
      graph.append(row)
      idx += 1

    matrix = preProcess(n, h, graph)
    ret = []
    for j in range(q):
      [s, e] = [int(x) for x in data[idx].split(" ")]
      idx += 1
      ret.append(str(round(matrix[s-1][e-1],8)))
    print("Case #%d: %s" % (i, " ".join(ret)))
