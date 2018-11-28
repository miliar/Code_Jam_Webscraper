def solve(n):
  digits = [int(c) for c in str(n)]
  solution = []
  prev = 0
  for idx, digit in enumerate(digits):
    if digit < prev:
      solution[-1] -= 1
      solution += [9 for _ in range(len(digits) - idx)]
      return solve(int(''.join(str(d) for d in solution)))
    else:
      solution.append(digit)
    prev = digit
  return int(''.join(str(d) for d in solution))

if __name__ == '__main__':

  num_cases = int(raw_input())
  for case in range(num_cases):
    n = int(raw_input())
    print 'Case #{}: {}'.format(case+1, solve(n))
