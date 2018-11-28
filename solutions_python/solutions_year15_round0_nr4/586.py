__author__ = 'pcjjman'
test = False
test_input = \
"""4
2 2 2
2 1 3
4 4 1
3 2 3"""
test_output = \
"""Case #1: GABRIEL
Case #2: RICHARD
Case #3: RICHARD
Case #4: GABRIEL"""

text_input = ""
if not test:
    num_cases = int(raw_input(""))
    #print "Saw {} cases".format(num_cases)
    text_input = ""
    cases = []
    for _ in range(num_cases):
        cases.append(raw_input(""))
    #print cases
else:
    cases = []
    num_cases = int(test_input.split('\n')[0])
    for i in range(num_cases):
        cases.append(test_input.split('\n')[i + 1])

output = ""
case_number = 1
for case in cases:
    #First make sure it is feasible by multiplying C * R and then checking whether the X is even divisible.
    #The case where Richard can choose a piece which may not be able to fit is more complex. For Richard to win, he has
    #to have a piece that regardless of rotation will not fit within C and R.
    #For a given length X, Richard can create a piece which is L1 wide (where L1 < X), and X+1-L1 long. If both L1 and X+1-L1
    #are > C or R regardless of rotation Gabriel cannot fit the piece in the rectangle.
    #If X >= 7, Richard always wins, as he can choose an X-omino in which there is an open space in the center but is
    # blocked on the sides, which makes it impossible for Gabriel to win.
    #And because it's an easy use case to check for, we have Gabriel win if the piece is X=1.
    #
    X, C, R = case.split(' ')
    X = int(X)
    C = int(C)
    R = int(R)
    #for calculation purposes we will have C always be the smaller
    if R < C:
        R, C = C, R
    winner = ""
    #easy case, if X is 1 or X is 2 and the number of spots on the board is even, Gabriel wins
    if X == 1 or (X == 2 and C * R % 2 == 0):
        winner = "GABRIEL"
    #check to make sure it's not a >= 7 (hole in piece), it can fill the spots in the rectangle, and that a straight piece
    #isn't longer than the longest side
    elif X >= 7 or (C * R) % X != 0 or X > R:
        winner = "RICHARD"
    #now comes the logic for the hardest one (checking to see if an L piece could not fit)
    else:
        if (C+C-1) < X:
            winner = "RICHARD"
        else:
            winner = "GABRIEL"
    #ignoring ftm
    case_output = "Case #{}: {}".format(case_number, winner)
    print case_output
    output += case_output + "\n"
    case_number += 1

if test:
    assert test_output.strip() == output.strip()