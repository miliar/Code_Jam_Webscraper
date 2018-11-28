from os import path

def solve_case(cj_input):
    """
    Solves one case of this CodeJam task and returns its solution.
    Read a line by calling 
       next(cj_input)
    """
    (min, max) = map(int, next(cj_input).split(" "))
    recycled_numbers = []
    for i in range(min, max):
        # some initial checks. even numbers cant be recycled numbers
        iStr = str(i)
        
        # swap around different combinations and check if in range
        for swapSize in range(1, len(iStr)):
            candidate = int(iStr[-swapSize:] + iStr[:-swapSize])
            if (candidate > i and candidate <= max):
                recycled_numbers.append((i, candidate))
        
    #for yay in recycled_numbers:
    #    print(yay)
    return str(len(recycled_numbers))


# From here on, the fairly generic CodeJam code follows. Read in file, output solutions.
# Potentially the first line does not include number of cases, this may have to be adapted.

def run_codejam():
    """
    Runs the codejam by initializing input and output, calling methods which solve the cases and finally
    outputting the results.
    """
    testfile = "C-small-attempt0"
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