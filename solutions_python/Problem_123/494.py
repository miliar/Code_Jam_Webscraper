import sys

def solve(A, motes, op_num):
  if not motes:
    return op_num

  # Cannot absorb
  if A <= motes[0]:
    add = -1
    if A > 1:
      # Add smaller mote
      add = solve(A + (A - 1), motes, op_num + 1)

    # Remove larger mote
    remove = solve(A, motes[1:], op_num + 1)

    if add != -1:
      return min(add, remove)
    return remove

  return solve(A + motes[0], motes[1:], op_num)

def output(case, min_op):
  print('Case #{}: {}'.format(case, min_op))

if __name__ == '__main__':
  d = 'small'
  # d = 'large'

  num_tests = int(sys.stdin.readline())

  for i in range(num_tests):
    [A, N] = [int(x) for x in sys.stdin.readline().split()]
    motes = [int(x) for x in sys.stdin.readline().split()]
    motes.sort()
    min_op = solve(A, motes, 0)
    output(i + 1, min_op)
