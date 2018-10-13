import os
import collections
import copy


def parse(input_filename):
    dataSet = {}
    with open(input_filename) as f:
        nbTestCase = int(f.readline())
        for i in range(1, nbTestCase+1):
            f.readline()
            dataSet[i] = collections.Counter([int(val) for val in f.readline().split()])
    return dataSet


def reduce(steps, counter):
    pmin = min(counter)
    npmin = counter[pmin]
    totalnpmin = npmin
    for p, n in counter.items():
        if p == pmin:
            continue
        totalnpmin += n*(p/pmin)
    if opti(pmin, totalnpmin)[0] == 1:
        newcounter = collections.Counter()
        for val in counter:
            if val == pmin:
                continue
            newcounter[val-pmin] = counter[val]
        return reduce(pmin+steps, newcounter)        
    return steps, counter
    
    
def opti(pancakes, n):
    res = (1, pancakes)
    for x in range(2, pancakes/2):
        temp = pancakes/x + int(bool(pancakes%x)) + n*(x-1)
        if res[1] > temp:
            res = (x, temp)       
    return res


def solve(counter, n=0, current_min = 999999, abs_min = 999999):
    pmax = max(counter)
    npmax = counter[pmax]

    current_min = 999999
    if pmax + n > current_min:
        return current_min
    current_min = res = pmax + n
    
    for x in range(2,pmax/2+1):
        newcounter = copy.copy(counter)
        del newcounter[pmax]
        newcounter[x] += npmax
        newcounter[pmax-x] += npmax
        res = min(res, solve(newcounter, n+npmax, current_min))
        
    return res
        
    
    
def solveAll(input_filename): 

    output_filename = os.path.splitext(input_filename)[0] + ".out"  
    dataSet = parse(input_filename)
    with open(output_filename, "w") as f:
        for k, data in dataSet.items():
            f.write("Case #{}: {}\n".format(k, solve(data)))

        
[solveAll(filename) for filename in os.listdir(".") if os.path.splitext(filename)[1] == ".in"]

# print(reduce(0, a))

# print(opti(104, 10))
