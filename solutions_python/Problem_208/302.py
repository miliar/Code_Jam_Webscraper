class node:
    def __init__(self, i, wt):
        self.i = i
        self.wt = wt
    def __lt__(self, other):
        return self.wt < other.wt
    def __le__(self, other):
        return self.wt <= other.wt

def pony(inname, outname):
    infile = open(inname, "r+")
    outfile = open(outname, "w+")
    lines = infile.readlines()
    T = int(lines[0])
    line_num = 1
    for t in range(T):
        N = int(lines[line_num].split(" ")[0])
        Q = int(lines[line_num].split(" ")[1])
        dists = []
        speeds = []
        line_num += 1
        for i in range(N):
            dists.append(int(lines[line_num].split(" ")[0]))
            speeds.append(int(lines[line_num].split(" ")[1]))
            line_num += 1
        adj_list = [[] for _ in range(N)]
        weights = [[0 for _ in range(N)] for _ in range(N)]
        for i in range(N):
            elements = lines[line_num].split(" ")
            for j in range(N):
                if (int(elements[j]) > -1):
                    adj_list[i].append(j)
                    weights[i][j] = int(elements[j])
            line_num += 1
        line_num += 1
        full_dist = [0 for _ in range(N)]
        for i in range(N-2, -1, -1):
            full_dist[i] = full_dist[i+1]+weights[i][i+1]
            for j in range(i+1, N):
                weights[i][j] = (float(full_dist[i]-full_dist[i+1])/speeds[i])+weights[i+1][j]
                for k in range(i+2, j+1):
                    if full_dist[i]-full_dist[k] <= dists[i]:
                        weights[i][j] = min(weights[i][j], (full_dist[i]-full_dist[k])/float(speeds[i])+weights[k][j])
        outfile.write("Case #" + str(t+1) + ": " + str(weights[0][N-1]) + "\n")
    infile.close()
    outfile.close()
