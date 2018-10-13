import fileinput
input = fileinput.input()
get = lambda t: list(t(i) for i in input.readline().strip().split())

def solve_case(casenum):
    N, s = get(str)
    N = int(N)
    shyness = [int(i) for i in s]
    result = 0
    clapping = 0
    for i, sh in enumerate(shyness):
        if clapping < i:
            result += i - clapping
            clapping = i
        clapping += sh
    print('Case #%s: %s' % (casenum+1, result))

T = get(int)[0]
for c in range(T):
    solve_case(c)


