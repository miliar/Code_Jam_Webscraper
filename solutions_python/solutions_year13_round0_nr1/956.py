#!/usr/bin/env python
# Benjamin James Wright
# Tic-Tac-Toek


def check_rows(Board):
    for e in ['X', 'O']:
        for i in xrange(0, 4):
            count = 0
            for j in xrange(0, 4):
                if A[i][j] == e or A[i][j] =='T':
                    count += 1
            if count == 4:
                return e
    return None

def check_columns(Board):
    for e in ['X', 'O']:
        for i in xrange(0, 4):
            count = 0
            for j in xrange(0, 4):
                if A[j][i] == e or A[j][i] == 'T':
                    count += 1
            if count == 4:
                return e
    return None
def check_diagonals(Board):
    for e in ['X', 'O']:
       count = 0
       for i in xrange(0, 4):
           if A[i][i] == e or A[i][i] == 'T':
               count += 1
       if count == 4:
           return e

       count = 0
       for i in xrange(0, 4):
           if A[i][3-i] == e or A[i][3-i] == 'T':
               count += 1
       if count == 4:
           return e
    return None

def solve(case, Board):
    case = case + 1
    # Find a winner
    result = result = check_rows(Board)
    if not result:
        result = check_columns(Board)
        if not result:
            result = check_diagonals(Board)
    # We have found a winner.
    if result:
        print("Case #" + str(case) + ": " + result + " won")
    # Draw
    elif '.' in Board[0] or '.' in Board[1] or '.' in Board[2] or '.' in Board[3]:
        print("Case #" + str(case) + ": Game has not completed")
    # Game still in play
    else:
        print("Case #" + str(case) + ": Draw")


# Retrieve the input
n = input()
for i in xrange(0, n):
  
    A = [list(raw_input()),
         list(raw_input()),
         list(raw_input()),
         list(raw_input())]
    if i < n - 1:
        raw_input() # Ignore a line
    solve(i, A)
