


def go(R, k, N, G):
  # print 'k =',k
  
  
  S = [0]
  for i in xrange(len(G)):
    S.append(S[-1] + G[i])
    
  #      0  1  2  3
  # G = [1, 4, 2, 1]
  # S = [0, 1, 5, 7, 8]
  # sum(2, 4) = 2+1 + 1+4
  #           = (8-5)       + (5-0)
  #           = S[-1]-S[2]  + S[4-2]
  #           = S[-1]-S[2]  + S[4-(4-2)]
  def sum(start, l):
    l = min(l, len(G))
    # print 'sum(%s, %s)' % (start, l)
    if start+l > len(G):
      return (S[-1] - S[start]) + \
             S[l-(len(G)-start)]
    else:
      return S[start+l] - S[start]
    
  # print G
  # print S
  
  pos  = 0
  euro = 0
  for r in xrange(R):
    start = 0
    end = len(G)+1
    while end-start > 1:
      m = (start+end)/2
      s = sum(pos, m)
      # print start, end, m, s
      if s > k: end   = m
      if s <=k: start = m

    
    e = sum(pos, start)
    assert e <= k
    # print '%d people %d:%d' % (e, pos, pos+start),
    # print G[pos:pos+start]
    
    
    euro += e
    pos = (pos+start) % len(G)
    
    
    
  
  return euro

T = int(raw_input())
for t in xrange(T):
  a = map(int,raw_input().split())
  a.append((map(int,raw_input().split())))
  print 'Case #%d: %s' % (t+1, go(*a))
  