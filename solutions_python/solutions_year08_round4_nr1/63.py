import sys

INTERIOR = 0
LEAF = 1
def parseInput(fname):
  f = open(fname, 'r')
  text = f.readlines()
  f.close()

  testCases = []
  cases = int(text[0])
  cnt = 1
  for i in range(cases):
    tmp = text[cnt].split(" ")
    numNodes = int(tmp[0])
    target = int(tmp[1])
    cnt += 1

    nodes = []
    for j in range((numNodes-1)/2):
      # read in interior node
      tmp = text[cnt].split(" ")
      nodes.append([INTERIOR, int(tmp[0]), int(tmp[1])])
      cnt += 1

    for j in range((numNodes-1)/2,numNodes):
      # read in leaf
      tmp = text[cnt]
      nodes.append([LEAF, int(tmp), -1])
      cnt += 1
      
    testCases.append((numNodes,target,nodes))
  return testCases


def runCase(case):
  #print "case"
  realans = []
  tryTarget(case[1], case[2], 0, [], realans)
  if realans:
    return min(realans)
  return "IMPOSSIBLE"

def tryTarget(target, nodes, numChanges, changed, res):
  ans, changes = traverseTree(0, nodes)
  #print target, ans, changes, numChanges, changed, nodes
  if ans == target:
    res.append(numChanges)
    return
  else:
    # change slightly
    while len(changes) > 0:
      flip = changes.pop()

      if flip[0] in changed:
        continue
      
      changed.append(flip[0])
      nodes[flip[0]][1] = not nodes[flip[0]][1]
      ans = tryTarget(target, nodes, numChanges+1, changed, res)
      nodes[flip[0]][1] = not nodes[flip[0]][1]
      changed.pop()
      # unflip, try next change
    return

AND = 1
OR = 0
def traverseTree(i,nodes):
  if nodes[i][0]==LEAF:
    return nodes[i][1],[]
  else:
    left, changes1 = traverseTree(i*2+1, nodes)
    right, changes2 = traverseTree(i*2+2, nodes)
    changes = changes1 + changes2
    if nodes[i][1] == AND:
      res = left and right
      other = -1
      if nodes[i][2]:
        # can change
        other = left or right
        if not other == res:
          changes.append([i, other])
      return res, changes
    else:
      res = left or right
      other = -1
      if nodes[i][2]:
        # can change
        other = left and right
        if not other == res:
          changes.append([i, other])
      return res, changes

def main(inputs=["test"]):
  for inputf in inputs:
    cases = parseInput(inputf+".in")
    res = []
    i = 1
    for case in cases:
      res.append((i,runCase(case)))
      i += 1
      
    output = ["\n".join("Case #%s: %s" % (num, ans) for num,ans in res)]
    print output
    outf = open(inputf+".out",'w')
    outf.write("\n".join("Case #%s: %s" % (num, ans) for num,ans in res))
    outf.close()

if __name__=="__main__":
  if sys.argv[1:]:
    main(sys.argv[1:])
  else:
    main()
