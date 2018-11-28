def solve(fin):
    D = int(fin.readline())
    P = [int(i) for i in fin.readline().split()]
    result = max(P)
    for i in range(1, max(P) + 1):
        S = 0
        for j in P:
            S += (j - 1) // i
        result = min(result, S + i)
    return result

def main():
    with open("input.txt") as fin, open("output.txt", 'w') as fout:
        t = int(fin.readline())
        for i in range(1, t + 1):
            print("Case #{0}: {1}".format(i, solve(fin)), file=fout)
    
main()