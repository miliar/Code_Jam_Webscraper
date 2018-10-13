import sys, itertools

lines_per_case = 2

def solve_case(case):
    points = [[-1 if c == '.' else int(c) for c in l.strip()] for l in case[1:]]
    results = []
    for i in range(len(points)):
        results.append(str(0.25 * get_wp(points, i) + 0.5 * get_owp(points, i) + 0.25 * get_oowp(points, i)))
        
    return '\n' + '\n'.join(results)
        
def get_wp(points, team, exclude=None):
    tot_games = len([p for p in points[team] if p > -1])
    won_games = len([p for p in points[team] if p == 1])
    if exclude is not None and points[team][exclude] > -1:
        tot_games -= 1
        if won_games > 0 and points[team][exclude] == 1:
            won_games -= 1
    return float(won_games)/float(tot_games)

def get_owp(points, team):
    ops = 0.
    wp = 0.
    for op, p in enumerate(points[team]):
        if p > -1:
            wp += get_wp(points, op, team)
            ops +=1
    return wp/ops

def get_oowp(points, team, cache={}):
    #if team in cache: return cache[team]
    ops = 0.
    owp = 0.
    for op, p in enumerate(points[team]):
        if p > -1:
            owp += get_owp(points, op)
            ops +=1
    cache[team] = owp/ops
    return owp/ops
            

def produce_output(index, solution):
    print 'Case #%s: %s' % (index, solution)


def get_test_cases(lines):
    x = 0
    while x < len(lines):
        y = x + int(lines[x])
        yield lines[x:y+1]
        x = y+1
        
if __name__ == "__main__":
    if(len(sys.argv) > 1):
        fn = sys.argv[1]
        with open(fn) as f:
            lines = f.readlines()
            nt = int(lines[0])
            for index, case in enumerate(get_test_cases(lines[1:]), 1):
                solution = solve_case(case)
                produce_output(index, solution)