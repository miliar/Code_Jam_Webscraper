def main():
    filename = "a"

    fin = open(filename + ".in", "r")
    fout = open(filename + ".out", "w")

    tests = int(fin.readline())
    for test in range(tests):
        smax, sarr = fin.readline().split()
        smax = int(smax)
        
        sum = 0
        ans = 0
        for i in range(smax + 1):
            if sum < i:
                ans += i - sum
                sum = i
            sum += int(sarr[i])
        
        print('Case #%d: %d' % (test + 1, ans), file=fout)

    fin.close()
    fout.close()

if __name__ == '__main__':
    main()