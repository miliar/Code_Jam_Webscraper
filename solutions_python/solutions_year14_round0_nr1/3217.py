# Google Code Jam (2013): Qualification Round

# Code Jam Utils
# Can be found on Github's Gist at:
# https://gist.github.com/Zren/5376385
from codejamutils import *

problem_id = 'A'

# problem_size = 'sample'
problem_size = 'small'
# problem_size = 'large'

opt_args = {
    # 'practice': True,
    'log_level': DEBUG,
    'filename': 'A-small-attempt0',
}




with Problem(problem_id, problem_size, **opt_args) as p:
    for case in p:
        info('Case', case.case)

        answer1 = case.readint() - 1
        grid1 = [case.readints() for row in range(4)]
        row1 = grid1[answer1]

        answer2 = case.readint() - 1
        grid2 = [case.readints() for row in range(4)]
        row2 = grid2[answer2]

        set1 = set(row1)
        set2 = set(row2)

        common = set1 & set2

        info(set1, set2)
        info(common)
        
        if len(common) >= 2:
            case.writecase('Bad magician!')
        elif len(common) == 1:
            case.writecase(list(common)[0])
        else:
            case.writecase('Volunteer cheated!')
