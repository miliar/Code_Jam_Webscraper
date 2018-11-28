#!/bin/bash

# pancake switcher application conglomerate suite


def read_problems(filename):
    problems = []
    f = open(filename, "r")
    try:
        N = int(f.readline())
        for i in range(N):
            state, K = f.readline().strip().split()
            problems.append([state, int(K)])
    finally:
        f.close()
    return(problems)


def switch(c):
    if c == "+":
        return("-")
    else:
        return("+")


def solve_problem(happy, K):
    # returns -1 for impossible
    steps = 0
    l = len(happy)
    # strings are immutable so need an array-like conversion
    happy = [(x == "+") for x in list(happy)]

    for i in range(l):
        if not happy[i]:
            if i + K <= l:
                # print("switching from %s at %d" % (happy, i))
                steps += 1
                for j in range(K):
                    happy[i + j] = not happy[i + j]
                # print("switched: %s" % happy)
            else:
                return("IMPOSSIBLE")
    return(steps)


def save_output(filename, solutions):
    f = open(filename, "w")
    try:
        case_index = 1
        for s in solutions:
            f.write("Case #%d: %s" % (case_index, str(s)))
            f.write("\n")
            case_index += 1
    finally:
        f.close()


if __name__ == "__main__":
    # problems = read_problems("A_test.txt")
    # problems = read_problems("A-small-attempt0.in")
    problems = read_problems("A-large.in")
    # print(problems)
    output = []
    for p in problems:
        res = solve_problem(p[0], p[1])
        # print(res)
        output.append(res)
    print(output)
    # save_output("A_test_solution.txt", output)
    # save_output("A_small_solution.txt", output)
    save_output("A_large_solution.txt", output)
