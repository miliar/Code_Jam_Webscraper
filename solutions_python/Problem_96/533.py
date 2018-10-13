
def main(filename):
    f = open(filename)
    ouf = open("2output.txt", "w")
    num_of_tests = int(f.readline())
    for test_i in range(num_of_tests):
        line = f.readline().split(" ")
        n = int(line[0])
        s = int(line[1])
        p = int(line[2])
        scores = [0] + map(int, line[3:])
        d = [[0 for col in range(n+1)] for row in range(n+1)]
        for j in range(1, n+1):
            d[0][j] = d[0][j-1]
            if scores[j] > (p - 1) * 3:
                print scores[j]
                d[0][j] += 1
        print d[0]
        for i in range(1, s+1):
            for j in range(1, n+1):
                d[i][j] = max(d[i][j], d[i][j-1])
                if scores[j] < (p - 1) * 3 - 1:
                    d[i][j] = max(d[i][j], d[i-1][j-1])
                elif scores[j] > (p - 1) * 3:
                    # p-2 p p
                    # p-1 p-1 p+1
                    d[i][j] = max(d[i][j], d[i][j-1] + 1, d[i-1][j-1] + 1)
                else:
                    # scores[j] = (p-1)*3-1 or scores[j] = (p-1)*3
                    # p-2 p-2 p
                    # p-2 p-1 p
                    if p>1:
                        d[i][j] = max(d[i][j], d[i-1][j-1] + 1)
                    else:
                        pass
        ans = max([0] + [d[i][n] for i in range(0, s+1)])
        ouf.write("Case #%d: %d\n" % (test_i + 1, ans))

if __name__ == "__main__":
    main("B-large.in.txt")
        
                
        
    