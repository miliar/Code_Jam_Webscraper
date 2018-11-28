#-*- enocding: utf-8 -*-
import sys

debug = False

def log(l):
    if debug:
        print(l)

def solve(cast, unify, oppose):
    unify_map = {}
    oppose_map = {}
    for r in unify:
        unify_map[tuple(r[:2])] = r[2]
        unify_map[tuple(reversed(r[:2]))] = r[2]

    for r in oppose:
        a, b = r
        oppose_map[a] = b
        oppose_map[b] = a

    log('%s\t%s\t%s' % (unify, oppose, cast))

    result_list = []
    for c in cast:
        result_list.append(c)

        while True:
            t = unify_map.get(tuple(result_list[-2:]))
            if t:
                result_list.pop()
                result_list[-1] = t
            else:
                break

        r = oppose_map.get(result_list[-1])
        if r and r in result_list[:-1]:
            result_list = []

        log ('%c\t%s' % (c, result_list))

    return result_list

if '__main__' == __name__:
    T = int(sys.stdin.readline().strip())

    for case_n in xrange(T):
        input_seq = sys.stdin.readline().strip().split()
        unify_string, oppose_string = [], []
        C = int(input_seq.pop(0))
        while C>0:
            C -= 1
            unify_string.append(input_seq.pop(0))
        D = int(input_seq.pop(0))
        while D>0:
            D -= 1
            oppose_string.append(input_seq.pop(0))
        N = int(input_seq.pop(0))
        cast = input_seq.pop(0)
        assert(input_seq == [])

        solution = solve(cast, unify_string, oppose_string)

        print('Case #%d: [%s]' % (case_n+1, ', '.join(solution)))
