
import time

g_question = "A"
# g_step = "sample"
# g_step = "small-attempt0"
g_step = "large"

g_file_in = g_question + "-" + g_step + ".in"
g_file_out = g_question + "-" + g_step + ".out" + "." + str(time.time())

g_problem_start = 0
g_problem_end = -1

g_validate = True


def error(message):
    import inspect, logging
    # Get the previous frame in the stack, otherwise it would be this function!!!
    func = inspect.currentframe().f_back.f_code
    # Dump the message + the name of this function to the log.
    logging.error("%s: %s in %s:%i" % (
        message,
        func.co_name,
        func.co_filename,
        func.co_firstlineno
    ))


def validate(problem, result):
    if not g_validate:
        return

## CODE


## CODE

class Problem:
    def __init__(self, N, D, horses):
        self.N = N
        self.D = D
        self.horses = horses

class Horse:
    def __init__(self, K, S):
        self.K = K
        self.S = S


    def calculateTime(self, D):
        self.T = (D - self.K)/self.S


from operator import attrgetter


def cruise_control(problem):
    horses = problem.horses
    for h in horses:
        h.calculateTime(problem.D)
    max_T_horse = max(horses, key=attrgetter('T'))

    return problem.D/(max_T_horse.T)


def solve(problem):

## CODE
    output = cruise_control(problem)

    validate(problem, output)

    return output

f_out = open(g_file_out, 'w')


def run():
    with open(g_file_in) as f_in:

## CODE
        num_problems = int(f_in.readline())
        i_problem = 1

        while True:
            line_i = f_in.readline()
            d_str, n_str = line_i.split(' ')
            N = int(n_str)
            D = float(d_str)
            horses = []

            for j_line in range(N):
                line_j = f_in.readline()
                line_j.split(' ')
                K, S = map(float, line_j.split(' '))
                horses.append(Horse(K, S))

            result = solve(Problem(N, D, horses))

            f_out.write("Case #{}: {}".format(i_problem, result))
            f_out.write('\n')

            i_problem += 1




run()

f_out.close()