# B.py - Tidy Numbers
# jreiter

for t in range(int(input())):
  n = input()
  dcount = 0
  prev = ''
  answer = "none"

  for i in range(len(n)):
    if n[i] == prev:
      dcount += 1
    elif n[i] > prev:
      dcount = 1
    elif n[i] < prev:
      j = i-(dcount)
      answer = n[:j] + str(int(n[j]) - 1) + (len(n)-j-1) * '9'
      break

    prev = n[i]

  if answer == "none":
    answer = n

  print("Case #{}: {}".format(t+1, int(answer)))

  #string_val = "x" * 10