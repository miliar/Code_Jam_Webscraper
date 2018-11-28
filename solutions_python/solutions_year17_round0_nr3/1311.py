import math

def RSLS(N,K):
    if(K == 1):
        return(math.ceil((N - 1)/ 2), math.floor((N - 1)/ 2))
    
    last = math.floor(math.log(K,2))
    depth = 0
    max_v = N
    max_c = 1
    while(max_v % 2 != 0 and depth < last):
        max_v = (max_v - 1) / 2
        max_c *= 2
        depth += 1
    if(depth == last):
        return(math.ceil((max_v -1)/ 2), math.floor((max_v - 1)/ 2))
    
    max_v = max_v / 2
    min_v = max_v - 1
    min_c = max_c
    for i in range(depth+1, last):
        if(max_v % 2 == 0):
            max_v = max_v / 2
            min_v = max_v - 1
            min_c = 2*min_c + max_c
        else:
            max_v = (max_v - 1) / 2
            max_c = max_c*2 + min_c
            min_v = max_v - 1

    if(K - pow(2,last) + 1 > max_c):
        return(math.ceil((min_v - 1)/ 2), math.floor((min_v - 1)/ 2))
    return(math.ceil((max_v - 1)/ 2), math.floor((max_v - 1)/ 2))

def main():
    infile = open("C-small-2-attempt0.in", "r")
    outfile = open("C-small-2-attempt0.out", "w")
    T = int(infile.readline())
    for i in range(T):
        line = infile.readline()
        line = line.split(" ")
        N = int(line[0])
        K = int(line[1])
        (maxs, mins) = RSLS(N,K)
        outfile.write("Case #"+str(i+1)+": "+str(maxs)+" "+str(mins)+"\n")

    infile.close()
    outfile.close()
