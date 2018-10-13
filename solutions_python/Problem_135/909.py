__author__ = 'rcarino'
import sys

def find_card(m1, r1, m2, r2):
    s1 = set(m1[r1-1])
    s2 = set(m2[r2-1])
    intersect = s1 & s2

    if len(intersect) == 1:
        return intersect.pop()
    elif len(intersect) > 1:
        return 'Bad magician!'
    else:
        return 'Volunteer cheated!'

with open(sys.argv[1]) as f:
# with open('magic_simple') as f:
    contents = f.readlines()
    for i in range(int(contents.pop(0))):
    # contents.pop(0)
    # for i in range(1):
        r1 = int(contents.pop(0))
        m1 = []
        for j in range(4):
            m1.append([int(n) for n in contents.pop(0).split(' ')])

        r2 = int(contents.pop(0))
        m2 = []
        for j in range(4):
            m2.append([int(n) for n in contents.pop(0).split(' ')])

        print 'Case #{0}: {1}'.format(i+1, find_card(m1, r1, m2, r2))