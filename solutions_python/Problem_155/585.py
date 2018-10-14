def solve(string):
  numbers = list(map(int, string))
  total = 0
  missing = 0
  for i,s in enumerate(numbers):
    missing = max(missing, i - total)
    total += s
  return missing

def main():
  cases = int(input())
  for i in range(1, cases+1):
    case = input().split(' ')[1]
    solution = solve(case)
    print('Case #{}: {}'.format(i, solution))

main()
