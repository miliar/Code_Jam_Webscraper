import sys

def get_case_input(inf):
    row = inf.readline().strip().split(' ')
    C, F, X = float(row[0]), float(row[1]), float(row[2])
    return C, F, X

def solve(C, F, X):
    rate = 2.0
    if X <= C:
        return X/rate

    x_prev = 0
    c_prev = 0
    ans = 0.0
    while True:
        x_time = X/rate
        if c_prev and (c_prev + x_time) > x_prev:
            ans += x_prev
            break 
        c_time = C/rate
        ans += c_prev

        rate += F
        x_prev, c_prev = x_time, c_time

    return ans

def main():
    infile = sys.argv[1]
    inf = open(infile, 'r')
    n_cases =  int(inf.readline())

    outfile = "cookie_out.txt"
    outf = open(outfile, 'w')

    for each in range(n_cases):
        C, F, X = get_case_input(inf)
        ans = solve(C, F, X)

        outline = 'Case #%s: %s'%(each+1, ans)
        outf.write(outline+'\n')

    outf.close()
    inf.close()


if __name__ == "__main__":
    main()
