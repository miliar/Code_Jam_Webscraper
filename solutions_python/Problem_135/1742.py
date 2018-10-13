from sys import stdin
rl = stdin.readline
T = int(rl())

def solve():
    return False

for t in xrange(T):
    row1 = int(rl())
    for i in xrange(4):
        temp = rl()
        if i == row1 - 1:
            first_answer = temp.split() 
    row2 = int(rl())
    for j in xrange(4):
        temp = rl()
        if j == row2 - 1:
            second_answer = temp.split()

    result = set(first_answer) & set(second_answer)
    if len(result) == 1:
        print 'Case #%d: %s' % (t + 1, list(result)[0])  
    elif len(result) == 0:
        print 'Case #%d: %s' % (t + 1, 'Volunteer cheated!')  
    else:
        print 'Case #%d: %s' % (t + 1, 'Bad magician!')  
