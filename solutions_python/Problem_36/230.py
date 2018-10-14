#-*- encoding: utf-8 -*-

import sys

def solve(substr, text, cache={}):
    s = cache.get((len(substr), len(text)), None)
    if s is not None:
        return s

    if len(text) == 0 or len(substr) > len(text):
        return 0

    if len(substr) == 1:
        return text.count(substr)

    first_occur = text.find(substr[0])
    if first_occur < 0:
        return 0
    trimmed = text[(first_occur+1):]

    solution = solve(substr, trimmed, cache) + solve(substr[1:], trimmed, cache)
    cache[(len(substr), len(text))] = solution
    return solution

if __name__ == '__main__':
    substr = 'welcome to code jam'
    case_n = int(sys.stdin.readline().strip())

    for i in range(case_n):
        cache = { }
        string = sys.stdin.readline().strip()
        n = solve(substr, string, cache)
        solution = '0000' + str(n)
        solution = solution[-4:]
        print 'Case #%d: %s' % (i+1, solution)
