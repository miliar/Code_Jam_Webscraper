# input example
# 3
# ---+-++- 3
# +++++ 4
# -+-+- 4

# output example
# Case #1: 3
# Case #2: 0
# Case #3: IMPOSSIBLE

def flip(k, index, string_array):

    if len(string_array) - index < k:
        return "IMPOSSIBLE"

    new_index = None
    for i in range(0, k):
        if string_array[index + i] == "+":

            if not new_index:
                new_index = index + i

            string_array[index + i] = "-"
        else:
            string_array[index + i] = "+"

    if not new_index:
        new_index = index + k

    return  new_index


def skip_done(index, string_array):
    new_index = index
    while new_index < len(string_array) and string_array[new_index] == "+":
        new_index += 1

    return new_index

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  s, k = [h for h in input().split(" ")]  # read a list of integers, 2 in this case
  k = int(k)

  index = 0
  flips = 0
  str_aray = [ letter for letter in s]
  while index < len(str_aray):
      index = skip_done(index, str_aray)
      if index == len(str_aray):
          break
      index = flip(k, index, str_aray)
      if index == "IMPOSSIBLE":
          break
      else:
          flips += 1

  if index == "IMPOSSIBLE":
      print("Case #{}: {}".format(i, index))
  else:
      print("Case #{}: {}".format(i, flips))
  # check out .format's specification for more formatting options