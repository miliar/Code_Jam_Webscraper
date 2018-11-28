#!/usr/bin/python

num_tests = int(raw_input())

def solve(A, B, K):
  if A < B: 
    A, B = B, A
  if K >= B: 
    return A*B
  num_bits_B = len(bin(B)) - 2
  B2 = 2**num_bits_B - 1
  B1 = 2**num_bits_B
  count = 0
  for a in xrange(A): 
    if a < K: 
      count += B
    elif a&B2 < K:
      count += B
    else: 
      count += K
      for b in xrange(K, B): 
        if a&b < K: 
          count += 1
  return count
  
if __name__ == '__main__': 
  for test_num in range(num_tests): 
    data = [int(x) for x in raw_input().split(" ")]
    A, B, K = tuple(data)
    print "Case #%d: %d" % (test_num+1, solve(A, B, K))
