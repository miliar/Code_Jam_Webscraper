from __future__ import division
LINES_PARAM = 0
INPUT_FILE_NAME = 'C-large.in'
OUTPUT_FILE_NAME = 'C-large.out'

import heapq as hq
inf = float('Inf')

def dijkstra(G, s):
    n = len(G)

    Q = [(0, s)]

    d = [inf for i in range(n)]
    d[s]=0


    while len(Q)!=0:
        (cost, u) = hq.heappop(Q)

        for v in range(n):
            if d[v] > d[u] + G[u][v] and G[u][v]!=-1:
                d[v] = d[u] + G[u][v]
                hq.heappush(Q, (d[v], v))
    return d
def distances(horses,dists):
    N=len(dists)
    fastest=[dijkstra(dists,i) for i in range(N)]
    for i in range(N):
        stamina=horses[i][0]
        speed=horses[i][1]
        for j in range(N):
            d=fastest[i][j]
            if d>stamina or d==-1:
                fastest[i][j]=inf
            else:
                fastest[i][j]/=speed
    return fastest
def do_case(parsed):
    N=parsed[0][0]
    Q=parsed[0][1]
    dists=distances(parsed[1:N+1],parsed[N+1:2*N+1])
    times=[0 for i in range(Q)]
    for i in range(Q):
        package=parsed[2*N+1+i]
        times[i]=dijkstra(dists,package[0]-1)[package[1]-1]
    return ' '.join([str(t) for t in times])

def do_parse(input):
    return [[int(num) for num in line.rstrip().split(" ")]for line in input]


def main():
    input_f = open(INPUT_FILE_NAME, 'r')
    output = []

    num_of_test_cases = int(input_f.readline(), 10)
    temp = input_f.readlines()
    index = 0
    for test_case in range(num_of_test_cases):
        lines = 2*int(temp[index].rstrip().split(" ")[0])+int(temp[index].rstrip().split(" ")[1])
        parsed_input = do_parse(temp[index:index + lines + 1])
        index = index + 1 + lines
        output.append('Case #' + str(test_case + 1) + ': ' + do_case(parsed_input))

    output_f = open(OUTPUT_FILE_NAME, 'w')
    output_f.write('\n'.join(output))

    input_f.close()
    output_f.close()


if __name__ == '__main__':
    main()
