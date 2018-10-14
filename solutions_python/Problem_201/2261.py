import math


def relevant_cases(N):
    rel_cases = {N}
    while (N - 1) % 2 == 0:
        N = int((N - 1) / 2)
        rel_cases = rel_cases | {N}
    if N == 1:
        rel_cases = rel_cases | {1, 0}
        rel_cases_lst = list(rel_cases)
        rel_cases_lst.sort()
        return rel_cases
    else:
        while N >= 3:
            case1 = int(math.floor((N - 1.0) / 2))
            case2 = int(math.ceil((N - 1.0) / 2))
            rel_cases = rel_cases | { case1 } | { case2 }
            if case1 % 2 == 0:
                N = case1
            else:
                N = case2
        rel_cases = rel_cases | {1, 0}
        rel_cases_lst = list(rel_cases)
        rel_cases_lst.sort()
        return rel_cases_lst

def interval_frequencies(N):
    interval_lengths = relevant_cases(N)
    freqs = { int_length : 0 for int_length in interval_lengths }
    freqs[N] = 1
    for length in interval_lengths[:0:-1]:
        freqs[math.floor((length - 1)/2)] = freqs[math.floor((length - 1)/2)] + freqs[length]
        freqs[math.ceil((length - 1)/2)] = freqs[math.ceil((length - 1)/2)] + freqs[length]
    return freqs

def solve(n, k):
    interval_lengths = relevant_cases(n)[::-1]
    freqs = interval_frequencies(n)
    for length in interval_lengths:
        if k <= freqs[length]:
            return math.ceil((length - 1)/2), math.floor((length - 1)/2)
        else:
            k = k - freqs[length]
    




#def solve(n, k):
#    if k > n/2:
#        return (0, 0)
#    n_cases = relevant_cases(n)
#    solutions = {n : {} for n in n_cases}
#    for n in solutions:
##        print("n = {}".format(n))
#        solutions[n][1] = [math.ceil( (n - 1)/2 ), math.floor( (n - 1)/2 ), 0, 0]
##        print("solutions = {}".format(solutions))
#        for no_guests in range(2, n + 1):
##            print("no_guests = {}".format(no_guests))
#            prev_sol = solutions[n][no_guests - 1]
##            print("prev_sol = {}".format(prev_sol))
#            if prev_sol[2] == math.floor( (n - 1)/ 2):
##                print("n = {}".format(n))
##                print("no_guests = {}".format(no_guests))
##                print("Hello!")
##                print("math.floor((n-1)/2) = {}".format(math.floor((n-1)/2)))
##                print("math.ceil((n-1)/2) = {}".format(math.ceil((n-1)/2)))
##                print("solutions = {}".format(solutions))
#                right_res = solutions[math.ceil( (n - 1)/2 )][prev_sol[3] + 1]
##                print("SPECIAL CASE")
##                print("n = {}".format(n))
##                print("no_guests = {}".format(no_guests))
#                solutions[n][no_guests] = [right_res[0], right_res[1], prev_sol[2], prev_sol[3] + 1]
##                print("solutions = {}".format(solutions))
#                continue 
##            print("math.floor((n-1)/2) = {}".format(math.floor((n-1)/2)))
##            print("math.ceil((n-1)/2) = {}".format(math.ceil((n-1)/2)))
##            print("n = {}".format(n))
#            left_res = solutions[math.floor( (n - 1)/2 )][prev_sol[2] + 1]
#            right_res = solutions[math.ceil( (n - 1)/2 )][prev_sol[3] + 1]
#            if left_res[1] < right_res[1]:
#                solutions[n][no_guests] = [right_res[0], right_res[1], prev_sol[2], prev_sol[3] + 1]
#            elif right_res[1] < left_res[1]:
#                solutions[n][no_guests] = [left_res[0], left_res[1], prev_sol[2] + 1, prev_sol[3]]
#            elif left_res[0] > right_res[0]:
#                solutions[n][no_guests] = [left_res[0], left_res[1], prev_sol[2] + 1, prev_sol[3]]
#            elif right_res[0] > left_res[0]:
#                solutions[n][no_guests] = [right_res[0], right_res[1], prev_sol[2], prev_sol[3] + 1]
#            else:
#                solutions[n][no_guests] = [left_res[0], left_res[1], prev_sol[2] + 1, prev_sol[3]]
##            print("solutions = {}".format(solutions))
#    answer = solutions[n][k]
#    return answer[0], answer[1]

cases = int(input())

for t in range(1, cases + 1):
    n, k = [int(s) for s in input().split(' ')]
    answer = solve(n, k)
    print("Case #{}: {} {}".format(t, answer[0], answer[1]))
