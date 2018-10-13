# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer


def is_tidy(a):
  if isinstance(a, str):
      for i in range(len(a)-1):
          if a[i] > a[i+1]:
            return False
      return True
  else:
      return is_tidy(str(a))


def get_le_tidy(a):
  if is_tidy(a):
      return a

  # first digit is always greater than 0
  for curr_d in range(len(a)-1, -1, -1):
    if a[curr_d] > '0':
      n = a[0:curr_d] + str(int(a[curr_d])-1) + ('9'*(len(a)-curr_d-1))
      if is_tidy(n):
          return n


for c in range(1, t + 1):
  n = input()
  r = get_le_tidy(n)
  print("Case #{}: {}".format(c, int(r)))
