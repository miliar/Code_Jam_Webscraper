def read(filename):
    f = open(filename)
    t = int(f.readline())

    cases = []

    for line in f:
        n, k = line.split(' ')
        cases.append((int(n), int(k)))

    return cases


def calculate(n, k):
    return k % (2 ** n) == 2 ** n - 1

def output(results):
    s = ''
    for i, result in enumerate(results):        
        s += 'Case #%i: %s' % (i + 1, 'ON\n' if result else 'OFF\n')
    return s
            
        
cases = read('A-large.in')

results = [calculate(*data) for data in cases]

open('pr1.out.txt', 'w').write(output(results))

