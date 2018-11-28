# Pancakes

def main():
    # Read in input
    num_test_case = int(input())

    for test_case in range(num_test_case):
        S, K = list(input().split())
        S = list(S)
        K = int(K)

        if K > len(S):
            print_solution(test_case, "IMPOSSIBLE")
            continue

        # Flip all "-" from left side
        flips = 0
        for idx in range(0, len(S) - K + 1):
            if S[idx] == "-":
                flips += 1
                for i in range(K):
                    if S[idx + i] == '-':
                        S[idx + i] = '+'
                    else:
                       S[idx + i] = '-'
        if '-' in S:
            print_solution(test_case, "IMPOSSIBLE")
        else:
            print_solution(test_case, str(flips))





def print_solution(case_number, solution_string):
    print("Case #{}: {}".format(case_number + 1, solution_string))

if __name__ == "__main__":
    main()
