#!/usr/bin/python3
num_cases = int(input())
for i in range(0,num_cases):
  data = input().split()
  N = int(data[0])
  K = int(data[1])
  row = 0
  while K >= 2 ** (row + 1):
    row += 1
  left_most = N
  # print(row)
  for j in range(0,row):
    if left_most % 2 == 0:
      left_most = (left_most / 2) - 1
    else:
      left_most = (left_most - 1) / 2
  # print("left_most: {}".format(left_most))
  num_larger_stalls = N - (((2 ** row) - 1) + (left_most * 2 ** row))
  # print("num_larger_stalls: {}".format(num_larger_stalls))
  remainder = K - (2 ** row - 1)
  # print("remainder: {}".format(remainder))
  if 0 < remainder <= num_larger_stalls:
    choice = left_most + 1
  else:
    choice = left_most
  # print("choice: {}".format(choice))
  if choice % 2 == 0:
    s_max = choice / 2
    s_min = (choice / 2) - 1
  else:
    s_max = (choice - 1) / 2
    s_min = (choice - 1) / 2
  s_max = str(s_max)
  s_min = str(s_min)
  s_max_str = ""
  s_min_str = ""
  for s in list(s_max):
    if s == ".":
      break
    s_max_str += s
  for s in list(s_min):
    if s == ".":
      break
    s_min_str += s
  print("Case #{}: {} {}".format(i + 1, s_max_str, s_min_str))

  #
  #
  # while K >= 2 ** row:
  #   new_sequences = []
  #   for stalls in sequences:
  #     if stalls % 2 == 0:
  #       new_sequences.extend([stalls / 2, stalls / 2 - 1])
  #     else:
  #       new_sequences.extend([(stalls - 1) / 2, (stalls - 1) / 2])
  #   sequences = list(new_sequences)
  #   row += 1
  #
  #
  #
  # for p in range(0,K):
  #   stalls = sequences.pop(0)
  #   if stalls == 1
  #   elif stalls % 2 == 0:
  #   else:
