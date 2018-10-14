class Node:
  def __init__(self, start, end):
    self.start = start
    self.end = end
    self.prev = None
    self.next = None


def chooseStalls(N, K):
  head = Node(-1, N)
  c = head
  for i in xrange(K - 1):

    range = c.end - c.start - 1
    if range == 1:
      if c is head:
        head = head.next
        c = head
      else:
        if c.next != None:
          c.next.prev = c.prev
        c.prev = c.next
        if c.next != None:
          c = c.next
        else:
          c = head
      continue
    if range == 0:
      raise Exception()
    if range % 2 == 0:
      mid = range / 2
    else:
      mid = range / 2 + 1
    right = Node(c.start + mid, c.end)
    right.next = c.next
    right.prev = c
    c.end = right.start
    c.next = right


    tt = c.start
    c.start = right.start
    right.start = tt

    tt = c.end
    c.end = right.end
    right.end = tt

    if right.end - right.start - 1 == 0:
      c.next = right.next

    c = right.next
    if c is None:
      c = head

  if c is None:
    c = head
  range = c.end - c.start - 1
  return range / 2, range - range / 2 - 1

def computeSpaces(arr, pos):
  left = 0
  i = pos - 1
  while i >= 0 and arr[i] == False:
    left += 1
    i -= 1
  right = 0
  i = pos + 1
  while i < len(arr) and arr[i] == False:
    right += 1
    i += 1
  return left, right

def bf(N, K):
  arr = [False] * N
  for k_ in xrange(K):
    s = {}
    for i in xrange(len(arr)):
      if not arr[i]:
        left, right = computeSpaces(arr, i)
        s[i] = (left, right)
    maxOfMin = []
    currentMaxOfMin = -1
    for v in s.itervalues():
      currentMaxOfMin = max(currentMaxOfMin, min(v[0], v[1]))
    for k, v in s.iteritems():
      if min(v[0], v[1]) == currentMaxOfMin:
        maxOfMin.append((v, k))
    if len(maxOfMin) == 1:
      arr[maxOfMin[0][1]] = True
      if k_ == K - 1:
        return max(maxOfMin[0][0]), min(maxOfMin[0][0])
    else:
      elem = max(maxOfMin, key=lambda asas: max(asas[0]))
      maxOfMax = []
      for m in maxOfMin:
        if max(m[0]) == max(elem[0]):
          maxOfMax.append(m)
      elem = min(maxOfMax, key=lambda it: it[1])
      arr[elem[1]] = True
      if k_ == K - 1:
        return max(elem[0]), min(elem[0])


T = input()
for t in xrange(T):
  N, K = map(int, raw_input().split(" "))
  r = bf(N, K)
  print "Case #" + str(t + 1) + ": " + str(r[0]) + " " + str(r[1])
