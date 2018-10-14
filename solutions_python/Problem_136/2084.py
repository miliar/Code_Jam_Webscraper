import sys
from codejam_utils import CodeJamProblem

def solve(fname):
    problem = CodeJamProblem(fname, "QB_solution.txt")

    test = problem.get_test()
    while test is not None:
        C,F,X = tuple([float(x) for x in test[0].strip().split(' ')])

        clickrate = 2.0
        total_time = 0.0
        wait = False

        while not wait:
            
            time_to_farm = C/clickrate
            time_to_goal = X/clickrate

            if time_to_goal < time_to_farm:
                total_time += time_to_goal
                wait = True
            elif X/(F + clickrate) <= time_to_goal - time_to_farm:
                clickrate = F + clickrate
                total_time += time_to_farm
            else:
                wait = True
                total_time += time_to_goal 

        problem.write_output('%.7f' %total_time)        
        test = problem.get_test()

solve(sys.argv[1])
    
