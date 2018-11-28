import sys

def main():
    infile = open(sys.argv[1], 'r')
    outfile = open(sys.argv[2], 'w')

    line = infile.readline()
    T = int(line)

    for t in range(1,T+1):
        A, B, K = infile.readline().strip("\n").split(" ")
        A = int(A)
        B = int(B)
        K = int(K)

        count = 0
        for i in range(0,A):
            for j in range(0,B):
                if (i & j) < K:
                    count += 1
        outfile.write("Case #{0}: {1}\n".format(t, count))

    infile.close()
    outfile.close()

if __name__ == '__main__':
    main()
