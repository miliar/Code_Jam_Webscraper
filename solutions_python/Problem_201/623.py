import heapq

def main(file_in, file_out):
    lines = file_in.readlines()[1::]
    writeSolution(file_out, [solve(getInts(line)) for line in lines])

def solve(row):
    N, K = row
    stalls = [-N]
    count = {N:1}
    minLR = -1
    maxLR = -1
    k = K
    while k > 0:
        x = -heapq.heappop(stalls)
        minLR = (x-1) // 2
        maxLR = (x) // 2
        k -= count[x]
        if minLR > 0:
            if minLR in count:
                count[minLR] += count[x]
            else:
                count[minLR] = count[x]
                heapq.heappush(stalls, -minLR)
        if maxLR > 0:
            if maxLR in count:
                count[maxLR] += count[x]
            else:
                count[maxLR] = count[x]
                heapq.heappush(stalls, -maxLR)
    return "{} {}".format(maxLR, minLR)
        
def writeSolution(file, slns):
    lines = ["Case #{}: {}".format(n+1, slns[n]) for n in range(len(slns))]
    file_out.write('\n'.join(lines))

def getInt(line):
    return int(line.strip())

def getInts(line):
    return [int(token.strip()) for token in line.split()]

if __name__ == "__main__":
    with open("C-large.in", "r") as file_in, open("test.out", "w") as file_out:
            main(file_in, file_out)
            file_out.close()