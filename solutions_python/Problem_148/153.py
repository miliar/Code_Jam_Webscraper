
def num_of_discs_to_store(N,X,S):
  num_discs = 0
  
  S = sorted(S)
  i = 0
  j = N-1

  while i < j:
    if S[j] + S[i] <= X:
      j -= 1
      i += 1
    else:
      j -= 1 
    num_discs += 1

  if i == j:
   num_discs += 1

  return num_discs

if __name__ == '__main__':
  T = int(raw_input())

  for i in xrange(1,T+1):
    N,X = tuple(int(x) for x in raw_input().split())
    S = tuple(int(x) for x in raw_input().split())
    assert len(S) == N
    
    discs = num_of_discs_to_store(N,X,S)
    print "Case #%s: %s" % (i, discs) 
