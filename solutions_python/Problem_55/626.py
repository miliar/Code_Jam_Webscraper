def read(filename):
    f = open(filename)
    t = int(f.readline())

    cases = []

    i = 0
    while i < t:
        i += 1
        params = f.readline()
        groups = f.readline()
        cases.append((map(int, params.split(' ', 3)), map(int, groups.split(' '))))

    return cases

def calculate(params, groups):
    r, k, n = params

    cash = 0
    
    for i in range(r):
        passed = []
        total = 0
        for j in range(n):
            if not groups or total + groups[0] > k:
                break
            else:
                g = groups.pop(0)
                passed.append(g)
                total += g
                cash += g
        groups.extend(passed)

    return cash            

def output(results):
    s = ''
    for i, result in enumerate(results):        
        s += 'Case #%i: %i\n' % (i + 1, result)
    return s
            
        
cases = read('C-small-attempt0.in')

results = [calculate(*data) for data in cases]

open('pr2.out.txt', 'w').write(output(results))
