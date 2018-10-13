def time_to_X(C, F, X, n):
    time = 0
    
    for i in range(n+1):
        if i == n:
            time += X/(2 + n*F)
        else:
            time += C/(2 + i*F)

    return time

def optimise(C, F, X):
    time = time_to_X(C, F, X, 0)
    i = 0
    
    while time > time_to_X(C, F, X, i+1):
        i += 1
        time = time_to_X(C, F, X, i)
        
    return ("%.7f" % time)

input_f = open('B-small-attempt0.in', 'r')
output_f = open('B-small.out', 'w')

cases = int(input_f.readline())
case = 0
result = ''

for line in input_f:
    case += 1
    varis = [float(v) for v in line.split()]
    result += "Case #" + str(case) + ": " + optimise(varis[0], varis[1], varis[2])
    if case != cases:
        result += '\n'

output_f.write(result)

input_f.close()
output_f.close()
