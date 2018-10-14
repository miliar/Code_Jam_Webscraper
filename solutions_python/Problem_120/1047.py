'''
Created on Apr 26, 2013

@author: user
'''

import sys
import math
import scipy.optimize

def computeRings(radius, volume):
    def func(N):
        return 2*N**2 + 2*N*radius - N - volume
    def dFunc(N):
        return 4 * N + 2 * radius - 1
    #quadratic solution has rounding errors
    guess = ((-2*radius + 1) + math.sqrt(4*radius**2 - 4*radius + 8*volume + 1)) / 4
    return math.floor(scipy.optimize.newton(func, guess, dFunc, maxiter=500, tol=1e-10))
    

def processFile(fileName):
    results = []
    with open(fileName) as handle:
        trials = int(handle.readline().strip())
        for i in range(trials):
            radius, volume = [int(x) for x in handle.readline().strip().split(" ")]
            results.append(computeRings(radius, volume))     
    return results
   
   
def writeResults(results, fileName):
    with open(fileName, 'w') as handle:
        case = 1
        for result in results:
            handle.write('Case #{}: {}\n'.format(case, result))
            case += 1
            

def main():
    results = processFile(sys.argv[1])
    writeResults(results, sys.argv[2])

if __name__ == '__main__':
    main()
