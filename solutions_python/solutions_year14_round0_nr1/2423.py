#!/usr/bin/env python

def read_input():
    num_test_cases = input()
    test_cases = []
    for i in range(0, num_test_cases):
        first_answer = input()
        first_arrangement = [map(int, raw_input().split()) for j in range(0, 4)]
        second_answer = input()
        second_arrangement = [map(int, raw_input().split()) for j in range(0, 4)]
        test_cases.append((first_answer, first_arrangement, second_answer, second_arrangement))
    return test_cases

def process_test_case(first_answer, first_arrangement, second_answer, second_arrangement):
    candidates1 = set(first_arrangement[first_answer - 1])
    candidates2 = set(second_arrangement[second_answer - 1])
    candidates = candidates1.intersection(candidates2)
    if len(candidates) == 1:
        return candidates.pop()
    elif not len(candidates):
        return "Volunteer cheated!"
    else:
        return "Bad magician!"

def process_all_test_cases(test_cases):
    for i, test_case in enumerate(test_cases):
        print "Case #{}: {}".format(i + 1, process_test_case(*test_case))

if __name__ == "__main__":
    process_all_test_cases(read_input())