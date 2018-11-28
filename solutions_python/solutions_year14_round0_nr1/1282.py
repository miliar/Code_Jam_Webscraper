'''
Created on 12/04/14 
Code Jam 2014 QR-A
@author: manolo
'''

import sys
ifile = sys.stdin
ofile = open('./a.out', 'w')

def r():
    return ifile.readline()[:-1]
    
def w(what):
    ofile.write(what + '\n')

bad = 'Bad magician!'
cheat = 'Volunteer cheated!'

T = int(r())
for case in range(1,T+1):

    answer1 = int(r())
    cards1 = [r().split(' '), r().split(' '), r().split(' '), r().split(' ')]
    possible1 = set(cards1[answer1-1])

    answer2 = int(r())
    cards2 = [r().split(' '), r().split(' '), r().split(' '), r().split(' ')]
    possible2 = set(cards2[answer2-1])

    possible = possible1.intersection(possible2)
    
    if len(possible) == 0:
        w('Case #' + str(case) + ': ' + cheat)
    elif len(possible) == 1:
        w('Case #' + str(case) + ': ' + possible.pop())
    else: # len(possible) > 0
        w('Case #' + str(case) + ': ' + bad)

ofile.close

