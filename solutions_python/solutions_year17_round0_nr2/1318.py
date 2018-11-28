def fix_one_inversion(n):
  num_digits = len(n)
  for i in range(num_digits - 1):
    if (int(n[i]) > int(n[i + 1])):
      if (i == 0 and n[i] == '1'):
        return ['9'] * (num_digits - 1)

      n[i] = str(int(n[i]) - 1)
      return n[: i + 1] + ['9'] * (num_digits - i - 1)
  return n


t = int(input())

for case in range(1, t + 1):
  n = list(input())
  num_digits = len(n)
  for i in range(num_digits - 1):
    new_n = fix_one_inversion(n)
    if (''.join(new_n) == ''.join(n)):
      n = new_n[:]
      break
    n = new_n[:]

  print("Case #" + str(case) + ":", ''.join(n))
