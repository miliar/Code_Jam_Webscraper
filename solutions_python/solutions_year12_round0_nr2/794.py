'''
for a given total score T, the possible values of the tuples are:
  (X,X-2,X-2,True);  X  = (T + 4)/3;True -> Surprise
  (X,X-1,X-2,True); X = (T + 3)/3;True -> Surprise
  (X,X,X-2,True); X = (T + 2)/3;True -> Surprise
  (X,X-1,X-1,False); X = (T + 2)/3;False -> Not a Surprise
  (X,X,X-1,False); X = (T + 1)/3;False -> Not a Surprise
  (X,X,X,False); X = (T)/3;False -> Not a Surprise

  where X is a possible best score and  is always an integer.
  -----
  So the solution is to simply search the whole space of the solutions,
  while trying to maximize the p value by distributing surprises appropriately
  
'''
def possible_scores(Ti):
  if(Ti == 0):
    return [(0,0,0),-1,-1,-1,-1,-1]
  result = []
  for i in range(3):
    for j in range(i+1):
      T = (Ti + i + j)
      X = T/3
      if ( T%3 == 0 and X - i >= 0 and X - j >= 0 and X <= 10):
        result.append((X,X-j,X-i))
      else:
        result.append( -1 )

  return result

def solve(N, S, p, scores):
  for i in xrange(N):
    scores[i] = possible_scores(scores[i])

  init = [0,-1,S] # [ X > p , currentPlayer, Surprises left]
  result = 0
  nodes = [init]
  while len(nodes) > 0:
    answer,player,surprisesLeft = nodes.pop(0)

    #As this is going to exhaust all possibilities, we just need the best answer.
    if answer > result:
      result = answer

    for action in range(6):
      nextPlayer = player + 1
      nextAnswer = answer
      nextSurprisesLeft = surprisesLeft
      #If next Player exists, and has a valid action
      if ( nextPlayer < N and scores[nextPlayer][action] != -1):
        #If you can add him to the list of surprises
        if (action < 3 or surprisesLeft > 0):
          if(action >= 3):
            nextSurprisesLeft = surprisesLeft - 1
          if(scores[nextPlayer][action][0] >= p):
            nextAnswer = answer + 1
          nodes.append([nextAnswer , nextPlayer, nextSurprisesLeft])
          
  
  return result

def process_input(case):
  values = [int(element)for element in case.split(' ')]
  N = values[0]
  S = values[1]
  p = values[2]
  scores = values[3:]

  return solve(N, S, p , scores)

def main():
  T = int(raw_input())
  for i in range(1,T+1):
    case = raw_input()
    print "Case #%d: %d"%(i, process_input(case))

if __name__ == '__main__':
  main()