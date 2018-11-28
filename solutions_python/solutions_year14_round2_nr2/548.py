
def solve(A, B, K):
    array = []
    for a in xrange(A):
        for b in xrange(B):
            if a & b < K:
                array.append((a, b))

    return  len(array)




if __name__ == "__main__":
    with open('inputB.txt', 'r') as infile, open('outputB.txt', 'w') as outfile:
        data = []
        for line in infile:
            data.append(map(int, line.split()))

        N = int(data[0][0])
        for n in xrange(N):
            A, B, K = data[n+1]
            str = "Case #{0}: {1}\n".format(n+1, solve(A,B,K))
            outfile.write(str)

