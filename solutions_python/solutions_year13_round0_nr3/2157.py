import io, math

# def print_solution(N, A, B):
#   C, D = A, B
#   C, D = int(math.floor(A)), int(math.ceil(B))
#   E, F = int(str(C)[:len(str(int(math.floor(C/2))))]), int(str(D)[:len(str(int(math.floor(D/2))))])
#   n = 0
#   for i in xrange(E, F+1):
#     print i
#     j = str(i)
#     j += j[::-1]

#     k = long(j)

#     if C <= i <= D:
#       l = str(k**2)
#       if l == l[::-1]:
#         print l
#         n += 1

#     if C <= k <= D:
#       l = str(k**2)
#       if l == l[::-1]:
#         print l
#         n += 1

#     for p in xrange(10):
#       j = str(i)
#       j += str(p) + j[::-1]
#       k = long(j)

#       if C <= k <= D:
#         l = str(k**2)
#         if l == l[::-1]:
#           print l
#           n += 1
#   print "Case #{0}: {1}".format(N, n)

# def solution(A, B):
#   i = A
#   n = 0
#   while i <= B:
#     si = str(i)
#     if si == si[::-1]:
#       j = int(math.sqrt(i))
#       sj = str(j)
#       if sj == sj[::-1]:
#         n += 1
#         print i
#     i += 1
#   return n

def solution(A, B):
  C = long(math.floor(math.sqrt(A)))
  D = long(math.ceil(math.sqrt(B)))
  i = C
  n = 0
  while i <= D:
    si = str(i)
    if si == si[::-1]:
      j = i**2
      sj = str(j)
      if sj == sj[::-1] and (A <= j <= B):
        n += 1
    i += 1
  return n

def main():
  N = int(raw_input())
  for testcase in xrange(1, N+1):
    A, B = map(long, raw_input().split())
    print 'Case #{0}: {1}'.format(testcase, solution(A, B))

if __name__ == '__main__':
  main()
