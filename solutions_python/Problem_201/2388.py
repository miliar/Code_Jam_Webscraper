import sys

def stalls(N, K):
    occupied = [True] + [False] * N + [True]
    distances = [(-1, N)] + [(i, N - i - 1) for i in range(N)] + [(N, -1)]
    
    for i in range(K):
        index = max([j for j in range(1, N + 1)], key=lambda x: (1 - int(occupied[x]), min(distances[x]),max(distances[x]), -x))
        occupied[index] = True
        for j in range(index - 1, 0, -1):
            if occupied[j]:
                break
            
            distances[j] = distances[j][0], index - j - 1
        
        for j in range(index + 1, N + 1):
            if occupied[j]:
                break
            
            distances[j] = j - index - 1, distances[j][1]
    return max(distances[index]), min(distances[index])
        
with open(sys.argv[1]) as infile:
    infile.readline()
    for index, line in enumerate(infile, 1):
        N, K = [int(x) for x in line.split()]
        print 'Case #%d:' % index, '%d %d' % stalls(N, K)
