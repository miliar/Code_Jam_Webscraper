import numpy as np

def determineWinner(x, r, c):
    if not r*c % x == 0:
        return 'RICHARD'
    if x <= 2:
        return 'GABRIEL'
    if r < 2 or c < 2:
        return 'RICHARD'
    if x == 3:
        return 'GABRIEL'
    if r < 3 or c < 3:
        return 'RICHARD'
    return 'GABRIEL'


for case in range(int(raw_input())):
    x, r, c = map(int, raw_input().split(' '))
    print 'Case #' + str(case+1) + ': ' + determineWinner(x, r, c)
