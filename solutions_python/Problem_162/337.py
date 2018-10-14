
def reverse_num(N):
    return int(str(N)[::-1])

def solve_test_case(N):
    # Looks like a dynamic programming question.
    # Just kidding. Work backwards.
    # Too hard: dynamic program up again...

    fastest = {1: 1}
    for idx in range(2, N+1):
        if reverse_num(idx) < idx and idx % 10 != 0:
            fastest[idx] = min(fastest[reverse_num(idx)], fastest[idx - 1]) + 1
        else:
            fastest[idx] = fastest[idx - 1] + 1
    return fastest[N]
        

print solve_test_case(1)
print solve_test_case(789012)
#print solve_test_case(12345678901234) # Supposedly 31000367?

def solve_problem(file_name):
    # Create the files and open them.
    input_file = file_name + ".in"
    output_file = file_name + ".out"
    f = open(input_file, "r")
    g = open(output_file, "w")

    # Get test cases:
    num_test_cases = int(f.readline())
    for test_case in range(1, num_test_cases + 1):
        N = int(f.readline())
        answer = solve_test_case(N)
        print N, answer
        g.write("Case #" + str(test_case) + ": " + str(answer) + "\n")

solve_problem("A-small-attempt1")
