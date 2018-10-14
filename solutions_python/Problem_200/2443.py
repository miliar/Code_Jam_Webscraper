def solve(x):
    solution = 0
    num_digits = len(str(x))
    c = num_digits
    add_count = 0
    
    while c > 0 and add_count < 9:
        to_add = int("1" * c)
        if solution + to_add <= x:
            solution += to_add
            add_count += 1
        else:
            c -= 1
    
    return solution


def main():
    infile = open('B-large.in')
    n = int(infile.readline())
    outfile = open('B-large.out', 'w')
    for i in range(1, n+1):
        line = infile.readline().strip()
        sol = solve(int(line))
        outfile.write("Case #{}: {}".format(i, sol) + '\n')

main()