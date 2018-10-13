#python 2.7

import sys
import math
import string
import itertools        

##def bestSwitchOption(dist, idx, q, e, s, Q, E, S, D, N):
##    bestCand = idx
##    testeddist = dist
##    for i in range(idx, N):
##        testedDist += D[i]
##        if (testedDist > e):
##            break
##        
##        qi = Q[i]
##        ei = E[i]
##        si = S[i]
##        if (ei >= (e - dist) and si >= s):
##            return i
##        
##    delta = D - k
##    return float(delta)/s

def solve(E, S, D, N):
    cityTimes = [-1] * N
    cityDist = [0]
    tot = 0
    for d in D[:-1]:
        tot += d
        cityDist.append(tot)
    print cityDist
    for i in range(N-2, -1, -1):
        #qi = Q[i]
        ei = E[i]
        si = S[i]
        
        start = cityDist[i]
        bestTime = float("inf")
        for j in range(i+1, N-1):
            delta = cityDist[j] - start
            if delta > ei:
                break
            time = delta/float(si)
            print str(delta) + "KM to " + str(j) + " at " + str(si) + " in: " + str(time) 
            bestTime = min(bestTime,cityTimes[j] + time)
        else:
            delta = cityDist[N-1] - start
            if (delta > ei):
                print "No hotshot possible for " + str(i)
            else:
                time = delta/float(si)
                print "Hotshot time " + str(i) + " -- " + str(time)
                bestTime = min(bestTime, time)
        cityTimes[i] = bestTime
        print bestTime

    return str(cityTimes[0])

    
def main():
    if (not len(sys.argv) == 3):
        print("Need exactly twos args: input filename and output filename")
        return
    input_data = open(sys.argv[1], 'r').read()
    output_file = open(sys.argv[2], 'w')
    split_input = input_data.split("\n")
    case_count = int(split_input[0])
    idx = 1
    case = 1
    while True:
        #print split_input[idx]
        N, Q = [int(x) for x in split_input[idx].split(' ')]
        idx += 1
        E = list()
        S = list()
        D = list()
        for i in range(0,N):
            e, s = [int(x) for x in split_input[idx].split(' ')]
            E.append(e)
            S.append(s)
            idx += 1
        for i in range(0,N):
            Delms = [int(x) for x in split_input[idx].split(' ')]
            d = -1
            for elm in Delms:
                if elm != -1:
                    d = elm
                    break
            D.append(d)
            idx += 1
        idx += Q
        print "Input, Case #" + str(case) + ": " + str([N,Q,E,S,D])
        res= solve(E, S, D, N)
        print "Result, Case #" + str(case) + ": " + str(res)
        output_file.write("Case #" + str(case) + ": " + str(res) + "\n")
        case += 1
        if (case > case_count):
            break
        
    
if __name__ == "__main__":
    main()
