import fileinput
import sys
import functools
import math

# 4x4
# X starts, O follows; they alternate
# the board MAY start with a T
# four in a row makes a win
# T counts as either an X or an O
# draw if board is full and no one won
# board position is either X, O, T, or .

# Ending statuses:
# "X won"
# "O won"
# "Draw"
# "Game has not completed"

# Output format:
# "Case #x: y"
# x is the case number (starting from 1)
# y is one of the above statuses

# Input:
# num_of_test_cases
# char char char char
# char char char char
# char char char char
# char char char char
# (empty line)

# encoding the board celverly:
# 0 1 2 3  --> + = 6
# 4 5 6 7
# 8 9 1011
# 12131415

# 2 3 5 7 --> * = 210
# 11 13 17 19
primes = [[2, 3, 5, 7],
          [11, 13, 17, 19],
          [24, 29, 31, 37],
          [41, 43, 47, 53]]

def mul(a, b):
  return a*b

def column(matrix, i):
    return [row[i] for row in matrix]

winning_values = []

primes_linear = primes[0] + primes[1] + primes[2] + primes[3]

# add rows
winning_values.append(reduce(mul, primes[0][0:4], 1))
winning_values.append(reduce(mul, primes[1][0:4], 1))
winning_values.append(reduce(mul, primes[2][0:4], 1))
winning_values.append(reduce(mul, primes[3][0:4], 1))

# add columns
winning_values.append(reduce(mul, column(primes, 0), 1))
winning_values.append(reduce(mul, column(primes, 1), 1))
winning_values.append(reduce(mul, column(primes, 2), 1))
winning_values.append(reduce(mul, column(primes, 3), 1))

# add diagonals
winning_values.append(primes[0][0] * primes[1][1] * primes[2][2] * primes[3][3])
winning_values.append(primes[0][3] * primes[1][2] * primes[2][1] * primes[3][0])


def see_if_board_is_a_win_for(bd, xORo):
  res = 1
  for ind, val in enumerate(bd):
    if val == xORo or val == 'T':
      res = res * primes_linear[ind]

  # see if res is divisible by any value in winning_values
  for val in winning_values:
    if res % val == 0:
      return True
  return False

 # if res in winning_values:
 #   return True
 # else:
 #   return False

def see_if_board_is_not_full(bd):
  return '.' in bd

def is_square(val):
  return math.sqrt(val).is_integer()

def is_square_of(val):
  return int(math.sqrt(val))

def is_fair(val):
  return str(val) == str(val)[::-1]

def see_result(bd):
  if see_if_board_is_a_win_for(bd, 'X'):
    return 'X won'
  if see_if_board_is_a_win_for(bd, 'O'):
    return 'O won'
  if see_if_board_is_not_full(bd):
    return  'Game has not completed'
  return 'Draw'

board = []
i = 0
case = 1
num = 0
firstone = True
for line in fileinput.input():
  if firstone:
    firstone = False
    continue
  interval = line.split()
  interval[0] = int(interval[0])
  interval[1] = int(interval[1])
  #print interval

  num = 0
  for v in range(interval[0], interval[1] + 1):
    if is_fair(v):
      if is_square(v):
        if is_fair(is_square_of(v)):
          num += 1
          # print str(v) + "has a palindromal square"
  print "Case #" + str(case) + ": " + str(num)
  case +=1
#  for ind, letter in enumerate(line):
#    if letter != '\n':
#      board.append(letter)
#      i+=1
#  #sys.stdout.write('\n')

# print(board)
#print "Case #" + str(case) + ": " + see_result(board)
