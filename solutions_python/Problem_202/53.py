from tqdm import tqdm
import networkx as nx
from networkx.algorithms import bipartite
from copy import deepcopy
from itertools import *

def solve():
  N, M = map(int, input().split())
  board = ['.'] * N
  for i in range(N):
    board[i] = ['.'] * N
  solution = deepcopy(board)

  cells = list(product(range(N), range(N)))

  for i in range(M):
    model, r, c = input().split()
    board[int(r)-1][int(c)-1] = model

  G = nx.Graph()

  G.add_nodes_from(range(N), bipartite=0)
  G.add_nodes_from(range(N, 2*N), bipartite=1)

  marked = set()
  for i, j in cells:
    if board[i][j] in ['x', 'o']:
      marked.add("r"+str(i))
      marked.add("c"+str(j))

  G.add_edges_from(
    [(i, j+N) for i, j in cells if board[i][j] not in ['x', 'o'] and
     "r{}".format(i) not in marked and "c{}".format(j) not in marked])

  #print (G.edges())
  matching = nx.bipartite.maximum_matching(G)
  #print (matching)
  for left, right in matching.items():
    if left < right:
      solution[left][right-N] = 'x'

  # for row in solution:
  #   print (''.join(row))
  # print()

  G.clear()

  G.add_nodes_from(range(-N-1, N-1 + 1), bipartite=0)
  G.add_nodes_from(range(N, 3 * N), bipartite=1)

  for i, j in cells:
      if board[i][j] in ['+', 'o']:
        marked.add("d1"+str(i-j))
        marked.add("d2"+str(i+j))

  edges = []
  for i, j in cells:
    if board[i][j] not in ['+', 'o']:
      d1 = i - j
      d2 = i + j
      if "d1{}".format(d1) not in marked and "d2{}".format(d2) not in marked:
        edges += [(d1, d2 + N)]

  G.add_edges_from(edges)

  matching = nx.bipartite.maximum_matching(G)
  #print (G)
  #print (matching)
  for left, right in matching.items():
    if left < right:
      i = (left + right-N) // 2
      j = (right-N - left) // 2
      if solution[i][j] != '.':
        solution[i][j] = 'o'
      else:
        solution[i][j] = '+'

  # for row in solution:
  #   print (''.join(row))

  for i, j in cells:
    if solution[i][j] == '.' and board[i][j] != '.':
      solution[i][j] = board[i][j]

  score = 0
  new = []

  for i, j in cells:
      if solution[i][j] != board[i][j]:
        if solution[i][j] != '.' and board[i][j] != '.':
          solution[i][j] = 'o'
          
        new.append("{} {} {}".format(solution[i][j], i + 1, j + 1))
      score += {"o":2,"x":1,"+":1,'.':0}[solution[i][j]]

  return {"score":score, "changed":len(new), "new": new}

if __name__ == "__main__":
  T = int(input())
  for t in tqdm(range(1, T + 1)):
    solution = solve()
    print ("Case #{}: {} {}".format(t, solution['score'], solution['changed']))
    for row in solution['new']:
      print(row)
