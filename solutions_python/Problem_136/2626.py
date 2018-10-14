import sys

def main(filename):
    with open(filename, 'r') as f_in:
        input_text = f_in.read().splitlines()

    T, case_list = int(input_text[0]), input_text[1:]
    output = []
    for i, case in enumerate(case_list):
        i += 1
        C, F, X = [float(x) for x in case.split()]
        # print solve(C, F, X)
        output.append("Case #{0}: {1:.7f}\n".format(i, solve(C, F, X)))
    with open('b.out', 'w') as f_out:
        f_out.writelines(output)

def solve(C, F, X):
    rate = 2.0
    wait_time = X/rate
    elapsed = 0

    while True:
        elapsed += C/rate
        rate += F
        buy_time = X/rate + elapsed
        if buy_time > wait_time:
            break
        wait_time = buy_time

    return min(wait_time, buy_time)

if __name__ == '__main__':
    main(sys.argv[1])

