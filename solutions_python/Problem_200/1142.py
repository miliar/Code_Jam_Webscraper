import sys
import os

def solve(x):
    print('------------------------')
    print('solving')
    print(x)
    result = ""
    rest = 0
    fix9 = False
    for i in range(len(x)-1):
        if fix9:
            x[i+1] = 9
        elif (x[i] < x[i+1]):
            rest = i+1
        elif (x[i] > x[i+1]):
            fix9 = True
            x[i+1] = 9
            x[rest] = x[i] - 1
            print('end %d %d' % (rest, i))
            for j in range(rest+1, i+1):
                x[j] = 9
    if x[0] == 0 and len(x) > 1:
        del x[0]
    for i in range(len(x)):
        result += str(x[i])
    return result

def main():
    print('=========================')
    with open(sys.argv[1]) as fp:
        def readline():
            return fp.readline().strip()
        num_cases = int(readline())
        with open(os.path.splitext(sys.argv[1])[0] + '.out', 'w') as fpo:
            for i in range(num_cases):
                x = [int(x) for x in readline()]
                res = "Case #%d: %s\n" % (i + 1, solve(x))
                print(res, end='')
                fpo.write(res)
main()
