import time

"""Idea: Use a stack to maintain the index of strictly increasing digits, read the number from left to right.
While the incoming number is strictly larger than the nums[top of the stack], push its index.
If it's equal, ignore it; if it's less, it means that we should decrement element at top of the stack by 1, and change everything after it to be 9.
e.g.
n    1234421
idx 0123456
stack: [0] -> [0, 1] -> [0, 1, 2] -> [0, 1, 2, 3] -> [0, 1, 2, 3] -> decrement 3 by 1 and everything else to 9 => 1233999
stack is not necessary
"""

def LastTidyNumber(N):
  """Returns the largest tidy number <= N.

  Args:
    N: The upper bound, represented as a string

  Returns:
    largest_tidy_number: The largest tidy number <= N
  """
  n_digits = len(N)
  if n_digits == 1: return N
  max_so_far = -1
  for idx in range(n_digits):
    if max_so_far < 0 or N[max_so_far] < N[idx]:
      max_so_far = idx
    elif N[max_so_far] > N[idx]:
      # Need to decrement st[-1] and flush the digits to its right with 9
      largest_tidy_number = N[:max_so_far] + chr(ord(N[max_so_far]) - 1) + '9' * (len(N) - max_so_far - 1)
      if largest_tidy_number[0] == '0': largest_tidy_number = largest_tidy_number[1:]
      return largest_tidy_number
  return N

start_time = time.time()
T = int(input())
for i in range(1, T + 1):
  N = input()
  largest_tidy_number = LastTidyNumber(N)
  print('Case #{}: {}'.format(i, largest_tidy_number))
with open('time.log', 'w') as f:
  f.write('--- %s seconds ---' % (time.time() - start_time))
  f.close()
