# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

def alphabet_cake(matrix, R, C):
  alphabet_dict = {} # alphabet: (row_low, row_high, column_low, column_high)
  for i in xrange(R):
    for j in xrange(C):
      candidate = matrix[i][j]
      if candidate != '?':
        if candidate in alphabet_dict:
          row_low, row_high, column_low, column_high = alphabet_dict[candidate]
          alphabet_dict[candidate] = (min(i, row_low), max(i, row_high), min(j, column_low), max(j, column_high))
        else:
          alphabet_dict[candidate] = (i, i, j, j)

  for alphabet in alphabet_dict:
    row_low, row_high, column_low, column_high = alphabet_dict[alphabet]
    for i in xrange(row_low, row_high + 1):
      for j in xrange(column_low, column_high + 1):
        matrix[i][j] = alphabet

  for alphabet in alphabet_dict:
    row_low, row_high, column_low, column_high = alphabet_dict[alphabet]

    for possible_column in xrange(column_high + 1, C):
      is_all_question = True
      for check_row in xrange(row_low, row_high + 1):
        if matrix[check_row][possible_column] != '?':
          is_all_question = False
          break
      if not is_all_question:
        alphabet_dict[alphabet] = (row_low, row_high, column_low, possible_column - 1)
        break
      else: 
        for row in xrange(row_low, row_high + 1):
          matrix[row][possible_column] = alphabet
        if possible_column == C - 1:
          alphabet_dict[alphabet] = (row_low, row_high, column_low, C-1)

    row_low, row_high, column_low, column_high = alphabet_dict[alphabet]
    for possible_column in xrange(column_low - 1, -1, - 1):
      is_all_question = True
      for check_row in xrange(row_low, row_high + 1):
        if matrix[check_row][possible_column] != '?':
          is_all_question = False
          break
      if not is_all_question:
        alphabet_dict[alphabet] = (row_low, row_high, possible_column + 1, column_high)
        break
      else: 
        for row in xrange(row_low, row_high + 1):
          matrix[row][possible_column] = alphabet
        if possible_column == 0:
          alphabet_dict[alphabet] = (row_low, row_high, 0, column_high)

  for alphabet in alphabet_dict:
    row_low, row_high, column_low, column_high = alphabet_dict[alphabet]

    for possible_row in xrange(row_high + 1, R):
      is_all_question = True
      for check_column in xrange(column_low, column_high + 1):
        if matrix[possible_row][check_column] != '?':
          is_all_question = False
          break
      if not is_all_question:
        alphabet_dict[alphabet] = (row_low, possible_row - 1, column_low, column_high)
        break
      else: 
        for column in xrange(column_low, column_high + 1):
          matrix[possible_row][column] = alphabet
        if possible_row == R - 1:
          alphabet_dict[alphabet] = (row_low, R-1, column_low, column_high)

    row_low, row_high, column_low, column_high = alphabet_dict[alphabet]
    for possible_row in xrange(row_low - 1, -1, - 1):
      is_all_question = True
      for check_column in xrange(column_low, column_high + 1):
        if matrix[possible_row][check_column] != '?':
          is_all_question = False
          break

      if not is_all_question:
        alphabet_dict[alphabet] = (possible_row + 1, row_high, column_low, column_high)
        break
      else: 
        for column in xrange(column_low, column_high + 1):
          matrix[possible_row][column] = alphabet
        if possible_row == 0:
          alphabet_dict[alphabet] = (0, row_high, column_low, column_high)

  return matrix


t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  R, C = [int(s) for s in raw_input().split(" ")]  
  matrix = []
  for j in xrange(R):
    matrix.append([])
    line = raw_input()
    for alphabet in line:
      matrix[j].append(alphabet)

  result = alphabet_cake(matrix, R, C)
  print "Case #{}:".format(i)
  for j in xrange(R):
    line_to_print = ''
    for k in xrange(C):
      line_to_print += result[j][k]
    print line_to_print
 # check out .format's specification for more formatting options