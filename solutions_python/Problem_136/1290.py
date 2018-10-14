import sys


def solve(cost, gainz, goal):
    production = 2.0
    result = goal / production
    old_result = result

    buying_time = 1/production
    while True:
        new_result = (goal/(production + gainz)) + cost*buying_time
        if new_result > result:
            return result
        production += gainz
        buying_time += 1/production
        result = new_result

    return result

if __name__ == '__main__':
    f = open(sys.argv[1], 'r')
    cases = int(f.readline())
    for i in range(cases):
        cost, production, goal = list(map(float, f.readline().split()))
        result = solve(cost, production, goal)
        print('Case #{0}: {1:.7f}'.format((i+1), result))
    f.close()
