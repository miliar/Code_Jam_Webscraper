# sadly, this is going to be an exercise in brute force
# sheet is a n*m array with elements 0, 1, 2, where 0 and 1 are b/w
# and 2 is used.
#
# sheet is [height][width]
# note m is height, n is width

import sys

def is_board(sheet, i, j, size):
  if i + size > len(sheet):
    return False
  if j + size > len(sheet[0]):
    return False
  start = sheet[i][j]
  if start == 2:
    return False
  for i_offset in range(size):
    for j_offset in range(size):
      color = sheet[i + i_offset][j + j_offset]
      if color == 2:
        return False
      # if offsets are 0, need color == start.  Then parity handles the rest.
      if (color + start + i_offset + j_offset) % 2:
        return False
  return True

def find_biggest_from_pos(sheet, i, j):
  for size in range(1, len(sheet) + 1):
    if not is_board(sheet, i, j, size):
      return size - 1
  return size

def find_biggest(sheet, hint):
  # should give minimal i, minimal j for the biggest
  # hint, if not none, should indicate a maximal possible size and an i at
  # which we should start looking for the size
  # hints don't appear to work correctly
  max_i = None
  max_j = None
  max_size = None
  if hint is not None:
    hint_i, hint_size = hint
    for i in range(hint_i, len(sheet)):
      for j in range(len(sheet[0])):
        size = find_biggest_from_pos(sheet, i, j)
        if size == hint_size:
          return (i, j, size)
  for i in range(len(sheet)):
    for j in range(len(sheet[0])):
      size = find_biggest_from_pos(sheet, i, j)
      if size > max_size:
        max_size = size
        max_i = i
        max_j = j
  return (max_i, max_j, max_size)

def cut_biggest(sheet, hint=None):
  i, j, size = find_biggest(sheet, hint)
  for i_offset in range(size):
    for j_offset in range(size):
      assert sheet[i + i_offset][j + j_offset] != 2
      sheet[i + i_offset][j + j_offset] = 2
  return size, i, j

def cut_all(sheet):
  # destructive to sheet
  remaining_squares = len(sheet) * len(sheet[0])
  result = dict()
  hint = None
  while remaining_squares:
    (size, i, j) = cut_biggest(sheet, None)
    hint = (size, i)
    if size == 1:
      result[1] = remaining_squares
      return result
    remaining_squares -= size**2
    result[size] = result.get(size, 0) + 1
  return result

def get_bit(a, bit):
  return (a >> bit) & 1

def parse_board(int_sheet, m, n):
  return [[get_bit(int_sheet, (m - i - 1) * n + (n - j - 1)) for j in range(n)] for i in range(m)]

def parse_row(row, n):
  rev_result = []
  for k in range(n):
    rev_result.append(row & 1)
    row = row >> 1
  rev_result.reverse()
  return rev_result

if __name__ == '__main__':
  t = int(sys.stdin.next())
  case_num = 0
  while True:
    case_num += 1
    m, n = map(int, sys.stdin.next().split())
    assert n % 4 == 0
    sheet = []
    for k in range(m):
      row = int('0x{0}'.format(sys.stdin.next()), 16)
      sheet.append(parse_row(row, n))
    result = cut_all(sheet)
    print "Case #{0}: {1}".format(case_num, len(result))
    for (size, num) in sorted(result.items(), reverse=True):
      print "{0} {1}".format(size, num)
    if case_num == t:
      break

