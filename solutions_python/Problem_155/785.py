import sys

def solve_case(case_num, line):
  line = line.split(' ')[1]
  nums = map(int, line)

  s = 0
  max_req = 0

  for ix, num in enumerate(nums):
    req = ix - s
    if req > max_req:
      max_req = req
    s = s + num

  print("Case #{}: {}".format(case_num, max_req))

if __name__ == "__main__":
  for case_num, case in list(enumerate(sys.stdin.read().splitlines()))[1:]:
    solve_case(case_num, case)
