

def solve_test_case(S_max, S):
    current_applause = 0
    help_needed = 0
    for idx in range(S_max + 1):
        candidates = int(S[idx: idx + 1])
        if current_applause >= idx:
            current_applause += candidates
        else:
            help_needed += idx - current_applause
            current_applause += candidates + idx - current_applause
    return help_needed

def solve_problem(input_file, output_file):
    f = open(input_file, "r")
    g = open(output_file, "w")

    # Get test cases:
    
    test_cases = int(f.readline())
    for test_case in range(1, test_cases + 1):
        S_max, S = f.readline().split()
        S_max = int(S_max)
        answer = solve_test_case(S_max, S)
        
        g.write("Case #" + str(test_case) + ": " + str(answer) + "\n")

solve_problem("A-large.in", "A-large.out")
