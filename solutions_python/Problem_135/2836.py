
def process_problem(problem):
    answer1 = int(problem[0])
    grid1 = problem[1:5]
    answer2 = int(problem[5])
    grid2 = problem[6:10]
    row1 = [int(x) for x in grid1[answer1 - 1].split(' ')]
    row2 = [int(x) for x in grid2[answer2 - 1].split(' ')]
    set1 = set(row1)
    answer = None
    for n in row2:
        if n in set1:
            if answer is not None:
                return 'Bad magician!'
            answer = n
    if answer is None:
        return 'Volunteer cheated!'
    return str(answer)

with open('A-small-attempt0.in', 'rb') as f:
    num_problems = int(f.next())
    for i in range(num_problems):
        problem = [f.next().strip() for j in range(10)]
        print 'Case #%d: %s' % (i + 1, process_problem(problem))

            
        
