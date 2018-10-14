def is_tidy(number):
  return sorted(number) == number

T = int(input())
for i in range(T):
  N = input()
  number = list(map(int, N))
  N = int(N)
  res = []
  while not is_tidy(number):
    number[-1] = 9
    number[-2] -= 1
    res.append(number[-1])
    del number[-1]
  number += res
  print('Case #'+ str(i+1) + ':',int(''.join(str(i) for i in number)))