
import sys

def transform_data(stdin):
    stdin.readline()
    cases = []
    for line in stdin:
        S_max, Si = line[:-1].split(" ")
        S_max = int(S_max)
        Si = list(map(lambda x: int(x), Si))
        cases.append((S_max, Si))
    return cases

def solution(stood_up_already, S_max, Si):
    if not Si: return 0
    if stood_up_already >= S_max - len(Si) + 1:
        return solution(stood_up_already + Si[0], S_max, Si[1:])
    else:
        inviting = S_max - len(Si) + 1 - stood_up_already
        return inviting + solution(stood_up_already + inviting + Si[0], S_max, Si[1:])

def solve(stdin):
    return map(lambda x: solution(0, *x), transform_data(stdin))

for i, result in enumerate(solve(sys.stdin), 1):
    print("Case #{i}: {result}".format(i=i, result=result))