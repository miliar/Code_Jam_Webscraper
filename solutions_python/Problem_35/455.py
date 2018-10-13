# -*- coding: utf-8 -*-
"""
Google Code Jam 2009
Qualification B
Watersheds
"""
# --- constants ---
North = 4
West = 3
East = 2
South = 1
Sink = -1
Labels = "abcdefghijklmnopqrstuvwxyz"
tmplabels = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# --- modules ---
import sys

# --- func ---
def cell_flow(map,h,w,H,W):
  # get the cell having the lowest attitude
  min = -1
  minpos = Sink
  # North cell
  if h > 0 and map[h-1][w] < map[h][w]:
    if min == -1 or min > map[h-1][w]:
      min = map[h-1][w]
      minpos = North
  # West cell
  if w > 0 and map[h][w-1] < map[h][w]:
    if min == -1 or min > map[h][w-1]:
      min = map[h][w-1]
      minpos = West
  # East cell
  if w+1 < W and map[h][w+1] < map[h][w]:
    if min == -1 or min > map[h][w+1]:
      min = map[h][w+1]
      minpos = East
  # South cell
  if h+1 < H and map[h+1][w] < map[h][w]:
    if min == -1 or min > map[h+1][w]:
      min = map[h+1][w]
      minpos = South
  # return result
  return minpos

# Label neighbor cells
def nbr_label(resMap,h,w,H,W):
  # North cell
  if h > 0 and resMap[h-1][w] == South:
    resMap[h-1][w] = resMap[h][w]
    nbr_label(resMap,h-1,w,H,W)
  # West
  if w > 0 and resMap[h][w-1] == East:
    resMap[h][w-1] = resMap[h][w]
    nbr_label(resMap,h,w-1,H,W)
  # East
  if w+1 < W and resMap[h][w+1] == West:
    resMap[h][w+1] = resMap[h][w]
    nbr_label(resMap,h,w+1,H,W)
  # South
  if h+1 < H and resMap[h+1][w] == North:
    resMap[h+1][w] = resMap[h][w]
    nbr_label(resMap,h+1,w,H,W)
  return

# label along given problem
def relabel(resMap,H,W):
  labeldic = dict()
  count = 0
  for h in range(H):
    for w in range(W):
      if labeldic.has_key(resMap[h][w]):
        resMap[h][w] = labeldic[resMap[h][w]]
      else:
        labeldic[resMap[h][w]] = Labels[count]
        resMap[h][w] = Labels[count]
        count += 1
  return


# --- main ---
# the number of maps
line = sys.stdin.readline().rstrip("\n")
T = int(line)

for t in range(T):
  line = sys.stdin.readline().rstrip("\n")
  params = line.split()
  H = int(params[0])
  W = int(params[1])
  Map = []
  # Get the map
  for h in range(H):
    line = sys.stdin.readline().rstrip("\n")
    Map.append(line.split())
  # Know relations between cells and which is a sink
  # the map for result
  resMap = []
  nsink = 0
  sinkpos = []
  for h in range(H):
    resMap.append([])
    for w in range(W):
      resMap[h].append(cell_flow(Map,h,w,H,W))
      # label sinks
      if resMap[h][w] == Sink:
        resMap[h][w] = tmplabels[nsink]
        sinkpos.append([h,w])
        nsink += 1

  # label cells
  for pos in sinkpos:
    nbr_label(resMap,pos[0],pos[1],H,W)
  relabel(resMap,H,W)
  # print result
  print "Case #"+str(t+1)+":"
  for h in range(H):
    resstr = ""
    for cell in resMap[h]:
      resstr += cell+" "
    print resstr
