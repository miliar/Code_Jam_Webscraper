import sys

num_cases = int(sys.stdin.readline())

for case_num in range(num_cases):
    case = sys.stdin.readline().split()
    A = int(case[0])
    B = int(case[1])
    num_solutions = 0
    for n in range(A,B):
        digits = str(n)
        solutions = []
        for location in range(1, len(digits)):
            if digits[location] == "0":
                continue
            m = int(digits[location:]+digits[:location])
            if n < m and m <= B:
                if m not in solutions:
                    solutions.append(m)
                    num_solutions += 1
    print "Case #"+str(case_num+1)+":", num_solutions
