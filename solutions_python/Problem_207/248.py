# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

def stable_neighbor(color_array):
  r_num = color_array[0]
  o_num = color_array[1]
  y_num = color_array[2]
  g_num = color_array[3]
  b_num = color_array[4]
  v_num = color_array[5]

  eff_r = r_num - g_num
  eff_y = y_num - v_num
  eff_b = b_num - o_num

  if eff_r < 0 or eff_y < 0 or eff_b < 0:
    return "IMPOSSIBLE"

  if eff_r == 0 and r_num > 0:
    if b_num == 0 and y_num == 0:
      result = 'RG' * r_num
    else:
      return "IMPOSSIBLE"
  if eff_y == 0 and y_num > 0:
    if r_num == 0 and b_num == 0:
      return 'YV' * y_num
    else:
      return "IMPOSSIBLE"
  if eff_b == 0 and b_num > 0:
    if y_num ==0 and r_num == 0:
      return "BO" * b_num
    else:
      return "IMPOSSIBLE"

  max_eff = max(eff_r, eff_y, eff_b)

  if max_eff * 2 > eff_r + eff_y + eff_b:
    return "IMPOSSIBLE"

  char_r_list = ['RG' * g_num + 'R'] + ['R'] * (eff_r - 1)
  char_y_list = ['YV' * v_num + 'Y'] + ['Y'] * (eff_y - 1)
  char_b_list = ['BO' * o_num + 'B'] + ['B'] * (eff_b - 1)

  result = ''
  if max_eff == eff_r:
    remaining = eff_y + eff_b - eff_r + 1
    result += char_r_list[0]
    if eff_y > eff_b:
      for i in xrange(remaining):
        if i % 2 == 0:
          result += char_y_list[i / 2]
        else:
          result += char_b_list[i / 2]

      for i in xrange(1, eff_r):
        result += char_r_list[i]
        if i - 1 < eff_y - (remaining + 1) / 2:
          result += char_y_list[i - 1 + (remaining + 1) / 2]
        else:
          result += char_b_list[i - 1 + remaining - eff_y]
    else:
      for i in xrange(remaining):
        if i % 2 == 0:
          result += char_b_list[i / 2]
        else:
          result += char_y_list[i / 2]

      for i in xrange(1, eff_r):
        result += char_r_list[i]
        if i - 1 < eff_b - (remaining + 1) / 2:
          result += char_b_list[i - 1 + (remaining + 1) / 2]
        else:
          result += char_y_list[i - 1 + remaining - eff_b]
    return result

  if max_eff == eff_b:
    remaining = eff_y + eff_r - eff_b + 1
    result += char_b_list[0]
    if eff_y > eff_r:
      for i in xrange(remaining):
        if i % 2 == 0:
          result += char_y_list[i / 2]
        else:
          result += char_r_list[i / 2]

      for i in xrange(1, eff_b):
        result += char_b_list[i]
        if i - 1 < eff_y - (remaining + 1) / 2:
          result += char_y_list[i - 1 + (remaining + 1) / 2]
        else:
          result += char_r_list[i - 1 + remaining - eff_y]
    else:
      for i in xrange(remaining):
        if i % 2 == 0:
          result += char_r_list[i / 2]
        else:
          result += char_y_list[i / 2]

      for i in xrange(1, eff_b):
        result += char_b_list[i]
        if i - 1 < eff_r - (remaining + 1) / 2:
          result += char_r_list[i - 1 + (remaining + 1) / 2]
        else:
          result += char_y_list[i - 1 + remaining - eff_r]
    return result

  if max_eff == eff_y:
    remaining = eff_b + eff_r - eff_y + 1
    result += char_y_list[0]
    if eff_b > eff_r:
      for i in xrange(remaining):
        if i % 2 == 0:
          result += char_b_list[i / 2]
        else:
          result += char_r_list[i / 2]

      for i in xrange(1, eff_y):
        result += char_y_list[i]
        if i - 1 < eff_b - (remaining + 1) / 2:
          result += char_b_list[i - 1 + (remaining + 1) / 2]
        else:
          result += char_r_list[i - 1 + remaining - eff_b]
    else:
      for i in xrange(remaining):
        if i % 2 == 0:
          result += char_r_list[i / 2]
        else:
          result += char_b_list[i / 2]

      for i in xrange(1, eff_y):
        result += char_y_list[i]
        if i - 1 < eff_r - (remaining + 1) / 2:
          result += char_r_list[i - 1 + (remaining + 1) / 2]
        else:
          result += char_b_list[i - 1 + remaining - eff_r]
    return result







t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  N, R, O, Y, G, B, V = [int(s) for s in raw_input().split(" ")]

  print "Case #{}: {}".format(i, stable_neighbor([R, O, Y, G, B, V]))

 # check out .format's specification for more formatting options