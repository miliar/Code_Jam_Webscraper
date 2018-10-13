# Template


def main():
    # Read in input
    num_test_case = int(input())

    for test_case in range(num_test_case):
        D, N = list(map(int, input().split()))

        horses = []
        for horse in range(N):
            horses.append(list(map(int, input().split())))

        # Compute for each horse when it reaches end
        time_to_reach = []
        for horse in horses:
            time_to_reach_dest = (D - horse[0]) / horse[1]
            time_to_reach.append(time_to_reach_dest)
        slowest = max(time_to_reach)
        max_speed = D / slowest
        print_solution(test_case, max_speed)




def print_solution(case_number, solution_string):
    print("Case #{}: {}".format(case_number + 1, solution_string))

if __name__ == "__main__":
    main()
