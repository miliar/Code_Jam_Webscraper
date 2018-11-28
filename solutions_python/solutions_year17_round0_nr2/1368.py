# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  n = [int(s) for s in list(str(input()))]  # read a list of integers, 2 in this case
  ok = False
  while not ok:
    k = n[0]
    ok = True
    for j in range(1, len(n)):
      if n[j] < k:
        n[j-1] = n[j-1] - 1
        for q in range(j, len(n)):
          n[q] = 9
        ok = False
        break
      else:
        k = n[j]
  print("Case #{}: {}".format(i, int("".join([str(w) for w in n]))))
  # check out .format's specification for more formatting options
 
