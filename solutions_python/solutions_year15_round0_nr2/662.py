import sys

def readline(line):
    l = line.strip('\n').split(' ')
    return [int(d) for d in l]

def reducestack(stacklist, maxstack):
    total_minutes = 0
    for stack in stacklist:
        minutes = (stack - 1) / maxstack
        total_minutes += minutes
    return total_minutes
    
def pancakes(stacklist):
    bigstack = max(stacklist)
    solution = bigstack
    for maxstack in xrange(bigstack, 1, -1):
        minutes = reducestack(stacklist, maxstack) + maxstack
        if minutes < solution:
            solution = minutes
    return solution
    
def main(file_in, file_out):
    results = []
    with open(file_in, 'r') as fin:
        T = int(next(fin).strip('n'))
        for x in xrange(T):
            next(fin)
            line = next(fin)
            stacklist = readline(line)
            result = pancakes(stacklist)
            results.append(result)
        
    with open(file_out, 'w') as fout:
        for case, result in enumerate(results, 1):
            line = 'Case #{}: {}\n'.format(case, result)
            fout.write(line)
            
            
    

if __name__ == '__main__':
    file_in = sys.argv[1]
    file_out = sys.argv[2]
    main(file_in, file_out)
    
    
