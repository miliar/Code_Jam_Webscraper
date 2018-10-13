#! /usr/local/bin/python
import itertools

def solve(case):
    result = [int(i) for i in case]

    for i in range(len(result) - 1):
        curr = result[i]
        nxt = result[i+1]
        if curr > nxt:
            while i > 0 and result[i-1] == curr:
                i -= 1

            for j in range(i+1, len(result)):
                result[j] = 9
            result[i] -= 1

            return int(''.join([str(e) for e in result]))
    return case


# def solve_old(case):
#     result = [int(i) for i in case]
#     for i in range(len(result)-2, -1, -1):
#         prev = result[i+1]
#         curr = result[i]
#         nxt = result[i-1]
#         print nxt, curr, prev
#
#         if curr > prev:
#             if i > 0:
#                 val = 9 if i == len(result)-2 else prev
#                 result[i+1] = val
#                 if curr > 0: # usual case
#                     result[i] = curr - 1
#                 else:
#                     if nxt > 0:
#                         result[i-1] -= 1
#                         result[i:] = itertools.cycle(9)
#                     else:
#                         val = int(''.join(result[:i-1]))
#                         result[:i-1] = list(str(val - 1))
#                         result[i] = prev
#             else:  # i == 0
#                 if curr == 1:
#                     return int(''.join([str(j) for j in result])) - 1
#                 else:
#                     result[0] = curr - 1
#                     result[1] = prev
#     return int(''.join([str(i) for i in result]))

n = int(raw_input())

cases = []
for i in range(n):
    cases.append(raw_input().strip())

output = []
for i, case in enumerate(cases):
    output.append('Case #{}: {}'.format(i+1, solve(case)))

print '\n'.join(output)
