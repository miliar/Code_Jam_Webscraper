#!/usr/bin/env python
import sys

if __name__ == '__main__':
    input_lines = [line.rstrip() for line in open(sys.argv[1] + ".in", "r").readlines()]
    output_file = open(sys.argv[1] + ".out", "w")

    num_test_cases = int(input_lines[0])
    test_cases = input_lines[1:]

    for test_num in xrange(len(test_cases)):
        test_case = test_cases[test_num].split(" ")
        
        combinations = {}
        num_combinations = int(test_case.pop(0))
        for combination_num in xrange(num_combinations):
            combination = test_case.pop(0)
            combined = combination[:-1]
            result = combination[-1]
            for permutation in [combined, combined[::-1]]:
                if not permutation in combinations.keys():
                    combinations[permutation] = result
        
        neutralisations = {}
        num_neutralisations = int(test_case.pop(0))
        for neutralisation_num in xrange(num_neutralisations):
            neutralisation = test_case.pop(0)
            for permutation in [neutralisation, neutralisation[::-1]]:
                if not permutation[0] in neutralisations:
                    neutralisations[permutation[0]] = permutation[1]

        num_elements = int(test_case.pop(0))
        elements = list(test_case.pop(0))
        invocation = []
        for element_num in xrange(num_elements):
            invocation.append(elements.pop(0))
            if len(invocation) > 1 and "".join(invocation[-2:]) in combinations.keys():
                invocation = invocation[:-2] + [combinations["".join(invocation[-2:])]]
            elif invocation[-1] in neutralisations and neutralisations[invocation[-1]] in invocation:
                invocation = []
        output_file.write("Case #{casenum}: [{invoked_result}]\n".format(casenum=test_num+1, invoked_result=", ".join(invocation)))
    
    output_file.close()
