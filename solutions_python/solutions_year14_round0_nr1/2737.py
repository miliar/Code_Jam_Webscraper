#!/usr/bin/python
'''
Google Code Jam 2014
Qualification Round
Problem A - Magic Trick
2014-04-11
Tyrus Tenneson
'''

import fileinput

def solve(case):
    ans1, arr1, ans2, arr2 = case
    result = set(arr1[ans1 - 1]).intersection(set(arr2[ans2 - 1]))
    if not result:
        return "Volunteer cheated!"
    if len(result) != 1:
        return "Bad magician!"
    return list(result)[0]

def main():
    lines = [l for l in fileinput.input()]
    T = int(lines[0])
    cases = []
    for case_start in map(lambda t: 10 * t + 1, range(T)):
        # Fuck, this was a dumb way to do this.
        cases.append((int(lines[case_start]),
                      tuple(map(lambda l: tuple(map(int, l.split())),
                                lines[case_start + 1 : case_start + 5])),
                      int(lines[case_start + 5]),
                      tuple(map(lambda l: tuple(map(int, l.split())),
                                lines[case_start + 6 : case_start + 10]))))
    for idx, case in enumerate(cases):
        print "Case #{}: {}".format(idx + 1, solve(case))
    
if __name__ == "__main__":
    main()
