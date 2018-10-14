DEBUG = False
DEBUG = True

def print_res(case, data):
  print("Case #{}: {}".format(case, data))


def get_tidy_num(num):
  for i in range(1, len(num)):
    if num[i] < num[i - 1]:
      num[i - 1] -= 1 
      num = get_tidy_num(num[:i]) + [9] * (len(num) - i)
      break

  return num


T = int(input())

for t in range(1, T + 1):
  N_raw = input()
  N = [int(x) for x in list(N_raw)]
  N_tidy = get_tidy_num(N)

  print_res(t, int(''.join(map(str, N_tidy))))
