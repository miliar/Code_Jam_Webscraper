T = int(raw_input())

def solve(A1, A2, R1, R2):

    solutions = 0
    solution = ''
    
    for number in R1[A1-1]:
        if number in R2[A2-1]:
            solutions = solutions + 1
            solution = number

    if solutions == 1:
        return solution
    elif solutions > 1:
        return 'Bad magician!'
    else:
        return 'Volunteer cheated!'

for i in xrange(1, T+1):
    A1 = int(raw_input())
    R1 = []
    for x in xrange(0,4):
        line = map(int, raw_input().split())
        R1.append(line)

    A2 = int(raw_input())
    R2 = []
    for x in xrange(0,4):
        line = map(int, raw_input().split())
        R2.append(line)

    print 'Case #' + str(i) + ': ' + str(solve(A1, A2, R1, R2))
    
