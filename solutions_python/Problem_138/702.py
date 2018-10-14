from itertools import permutations

def kenStrat(nao,ken):
  kenans = []
  kencp = ken[:]
  for i in nao:
    maxk = max(kencp)
    mink = min(kencp)
    if i > maxk:
      kenans.append(kencp.pop(kencp.index(mink)))
    else:
      for j in kencp:
        if j > i:
          kenans.append(kencp.pop(kencp.index(j)))
          break
  return kenans

def calcScore(naoAns,kenAns):
  score = [0,0]
  for i,e in enumerate(naoAns):
    if e > kenAns[i]:
      score[0]+=1
    else:
      score[1]+=1
  return score


def solve(nao,ken):
  nao.sort()
  ken.sort()
  
  scores = set([])
  kenansWar = kenStrat(nao[:],ken[:])
  scoreWar = calcScore(nao[:],kenansWar[:])[0]

  naoAnsWar = kenStrat(ken,nao)
  scoreNaoWar = calcScore(naoAnsWar,ken)[0]

  return [scoreNaoWar,scoreWar]

T = int(raw_input())
for i in range(T):
  raw_input()
  nao = map(float,raw_input().split())
  ken = map(float,raw_input().split())
  sol = solve(nao,ken)
  print 'Case #%d: %d %d' %(i+1 , sol[0] , sol[1])

