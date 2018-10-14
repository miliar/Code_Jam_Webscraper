# Template


def main():
    # Read in input
    num_test_case = int(input())

    for test_case in range(num_test_case):
        N, K = list(map(int, input().split()))
        U = float(input())
        p = list(map(float, input().split()))

        if N == 1:
            print_solution(test_case, "{}".format(min(1.0, p[0] + U)))
            continue

        p.sort()
        while U > 0.0:
            # Find lowest elements
            smallest = p[0]
            numbers = 0
            for i in range(N):
                if p[i] == smallest:
                    numbers += 1


            if numbers == len(p):
                for i in range(numbers):
                    p[i] += U / numbers
                break
            else:
                next_largest = p[numbers]

            # Distribute equally
            difference = next_largest - smallest
            if U > numbers*difference:
                for i in range(numbers):
                    p[i] += difference
                U -= difference*numbers
            else:
                for i in range(numbers):
                    p[i] += U / numbers
                break
        probability = 1
        for prob in p:
            probability *= prob
        print_solution(test_case, "{}".format(probability))









def print_solution(case_number, solution_string):
    print("Case #{}: {}".format(case_number + 1, solution_string))

if __name__ == "__main__":
    main()
