def solve(need, have):
    divisor = 1.0
    result = 0
    while True:
        con = 0
        valid = []
        removal_value = []
        for i in range(len(need)):
            removal_value.append([])
            valid.append(0)
            need_value = need[i]
            min_value = need_value * 0.9
            max_value = need_value * 1.1
            for j in range(len(have[i])):
                if min_value <= have[i][j] / divisor <= max_value:
                    valid[i] += 1
                    removal_value[-1].append(have[i][j])
                if min_value <= have[i][j] / divisor:
                    con += 1
        for i in range(len(have)):
            so = sorted(removal_value[i])
            for j in range(min(valid)):
                have[i].remove(removal_value[i][j])
        divisor += 1.0
        result += min(valid)
        if con == 0:
            break
    return result




def main():
    input_file_name = 'B-input.in'
    output_file_name = 'B-output.out'
    with open(input_file_name) as fin:
        with open(output_file_name, 'w') as fout:
            t = int(fin.readline())
            for tc in range(t):
                n, p = tuple(map(int, fin.readline().split()))
                need = list(map(int, fin.readline().split()))
                have = []
                for i in range(n):
                    have.append(list(map(int, fin.readline().split())))
                fout.write("Case #%d: %d\n" % ((tc + 1), solve(need, have)))
main()