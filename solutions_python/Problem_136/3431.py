import math
import copy
import logging
import string
import sys
sys.setrecursionlimit(10000000) # 10000 is an example, t

trace = logging.info

bestLocalSolution = 999999999

def bestTimePossible(elapsedTime, cookies, cookiesPerSecond, C, F, X):
    global bestLocalSolution
    if elapsedTime > bestLocalSolution:
        trace("found best Local solution: %s"%bestLocalSolution)    
        return bestLocalSolution
    trace("time: %s - cookies: %s/%s - CPS: %s"%(elapsedTime, cookies, X, cookiesPerSecond))
   
    ## cuanto tardaria esperar a ganar
    timeToWin = (X - cookies) / cookiesPerSecond;
    trace("timeToWin: %s"%timeToWin)
    if elapsedTime + timeToWin < bestLocalSolution:
        bestLocalSolution = elapsedTime + timeToWin
    
    ##cuanto tardaria esperar a comprar fabrica y esperar
    # si no nos alcanza para comprar fabrica, sumar tiempo
    if cookies < C:
        timeToNextFactory = (C - cookies) / cookiesPerSecond;
        elapsedTime = elapsedTime + timeToNextFactory 
        cookies = C
    
    # compramos todas las fabricas que podamos
    while cookies >= C:
        cookies = cookies - C
        cookiesPerSecond = cookiesPerSecond + F
    
    time = bestTimePossible(elapsedTime, cookies, cookiesPerSecond, C, F, X)
    if elapsedTime+time < bestLocalSolution:
        bestLocalSolution = elapsedTime+time
    return bestLocalSolution
    


def main(arg_file):
    global bestLocalSolution
    input = open(arg_file)
    nTestCases = int(input.readline())
    for testCase in range(0, nTestCases):
        cookies = 0
        cookiesPerSecond = 2
        [C, F, X] = [float(i) for i in input.readline().split(" ")]
        bestLocalSolution = 9999999999
        output = bestTimePossible(0, cookies, cookiesPerSecond, C, F, X)
        print "Case #%i: %s" % (testCase + 1, round(output, 7))
    input.close()


if __name__ == "__main__":
    logging.getLogger().setLevel(logging.CRITICAL)
    # descomentar para ver llamadas a trace()
    #logging.getLogger().setLevel(logging.INFO)
    main(sys.argv[1])
