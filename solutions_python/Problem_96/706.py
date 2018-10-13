from os import path, linesep
import itertools


def solve_case(cj_input):
    """
    Solves one case of this CodeJam task and returns its solution.
    Read a line by calling 
       next(cj_input)
    """
    # Necessary input of this case
    case_description = list(map(int, next(cj_input).split(" ")))
    googlers = case_description[0]
    surprising_triplets = case_description[1]
    best_result_boundary = case_description[2]
    scores = case_description[3:]
    
    # best result boundary is 0?
    if best_result_boundary <= 0:
        return str(googlers)
    
    # find out how many could have made it
    successful_googlers = 0     # what a horrible line :D
    potential_surprising_cases = 0
    for score in scores:
        # summed scored smaller than best result boundary, no way...
        if score < best_result_boundary:
            continue
        # looks successful, as ratings can be (p, p-1, p-1) with best result boundary p
        if score >= max(0, 3 * best_result_boundary - 2):
            successful_googlers += 1
        # could be a surprising case with sum >= (p, p-2, p-2)
        elif score >= max(0, 3 * best_result_boundary - 4):
            potential_surprising_cases += 1
    
    return str(successful_googlers + min(potential_surprising_cases, surprising_triplets))


# From here on, the fairly generic CodeJam code follows. Read in file, output solutions.
# Potentially the first line does not include number of cases, this may have to be adapted.

def run_codejam():
    """
    Runs the codejam by initializing input and output, calling methods which solve the cases and finally
    outputting the results.
    """
    testfile = "B-large"
    cases_file = path.join(path.dirname(__file__), testfile)
    with open(cases_file + ".in", "r") as cj_input:
        with open(cases_file + ".out", "w") as cj_output:
            # get a line-based reader
            reader = iter(cj_input.read().splitlines())
            
            # read number of cases
            caseCount = int(next(reader))
            
            # handle cases (1-based)
            for i in range(1, caseCount+1):
                result = solve_case(reader)
                outputStr = "Case #" + str(i) + ": " + result
                cj_output.write(outputStr + "\n")
                print(outputStr)
        
# run the CodeJam analysis
run_codejam()