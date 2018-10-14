number_of_cases = int(input())

for case in range(1, number_of_cases + 1):
  last_tidy_number = 1
  n = list(input())

  current_digit = 0
  while current_digit < len(n) - 1:

    current_val = int(n[current_digit])
    next_val = int(n[current_digit + 1])

    if current_val > next_val:
      n[current_digit] = str(current_val - 1)
      n[current_digit + 1:] = ['9' for i in range(len(n) - (current_digit + 1))]
      current_digit += 1
      continue

    if current_digit < len(n) - 2:
      lowest_next_val = int(min(n[current_digit + 2:]))
      if current_val > lowest_next_val:
        n[current_digit + 1] = str(next_val - 1)
        n[current_digit + 2:] = ['9' for i in range(len(n) - (current_digit + 2))]
        continue

    current_digit += 1

  print("Case #{}: {}".format(case, str(int(''.join(n)))))
