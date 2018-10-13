def solve(fin):
    Smax, S = fin.readline().split()
    Smax = int(Smax)
    S = [int(i) for i in S]
    result = 0
    standed = 0
    for i in range(Smax + 1):
        if standed < i and S[i]:
            result += i - standed
            standed = i
        standed += S[i]
    return result
    

def main():
    with open("output.txt", "w") as fout, open("input.txt") as fin:
        T = int(fin.readline())
        for i in range(T):
            print("Case #{0}: {1}".format(i + 1, solve(fin)), file=fout)
    
main()