import math
from heapq import heapify

def left(N):
    return int(math.floor((N - 1) / 2.0))

def right(N):
    return int(math.ceil((N - 1) / 2.0))

def recurse(N, K):
    if K < 1:
        return
    if K == 1:
        return str(right(N)) + " " + str(left(N))
    elif K == 2:
        return recurse(right(N), K - 1)
    else:
        return recurse(right(N), K - 1)
        return recurse(left(N), K - 2)

def iterate(N, K):
    consecutive_free_stalls = [-N]
    while K > 1:
        N_temp = -consecutive_free_stalls.pop()
        consecutive_free_stalls.append(-left(N_temp))
        consecutive_free_stalls.append(-right(N_temp))
        heapify(consecutive_free_stalls)
        consecutive_free_stalls.reverse()

        K -= 1

    free = -consecutive_free_stalls.pop()
    return str(right(free)) + " " + str(left(free))

def bathroom_stalls(inputfile, outputfile):
    fin = open(inputfile, "r")
    fout = open(outputfile, "w")
    no_of_cases = int(fin.readline())

    case_no = 1

    while case_no <= no_of_cases:
        N, K = fin.readline().strip("\n").split(" ")
        N = int(N)
        K = int(K)

        res = iterate(N, K)

        fout.write("Case #" + str(case_no) + ": " + res + "\n")

        case_no += 1

    fin.close()
    fout.close()

bathroom_stalls("C-small-1-attempt0.in", "C-small-1-attempt0.out")
