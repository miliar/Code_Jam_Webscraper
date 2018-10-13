# Google Code Jam (2013): Qualification Round

# Code Jam Utils
# Can be found on Github's Gist at:
# https://gist.github.com/Zren/5376385
from codejamutils import *

problem_id = 'B'

# problem_size = 'sample'
# problem_size = 'small'
problem_size = 'large'

opt_args = {
    #'practice': True,
    'log_level': DEBUG,
    'filename': 'B-large',
}


def total_time(C, F, X):
    cookies_per_second = lambda farms: 2 + farms * F
    farm_build_time = lambda cps: C / float(cps)
    win_time = lambda cps: X / float(cps)


    t = 0
    farms = 0

    while True:
        curCPS = cookies_per_second(farms)
        nextCPS = cookies_per_second(farms+1)

        farmT = farm_build_time(curCPS)

        curWT = win_time(curCPS)
        nextWT = farmT + win_time(nextCPS)

        # info(t, farms)

        if curWT > nextWT:
            # Buy a farm
            t += farmT
            farms += 1
        else:
            t += curWT
            return t



with Problem(problem_id, problem_size, **opt_args) as p:
    for case in p:
        info('Case', case.case)
        
        C, F, X = map(float, case.readline().split())

        case.writecase(total_time(C, F, X))