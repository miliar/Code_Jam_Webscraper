
def solve(D, N, h_list):
    time = 0.
    for start, speed in h_list:
        distance = D - start
        time = max(time, distance * 1. / speed)
    return D / time


if __name__ == "__main__":
    output = []
    fname = 'A-large'
    with open(fname + '.in') as f:
        inputs = [line.strip() for line in f]

    num_cases = int(inputs[0])
    line = [1]

    def next_line():
        text = inputs[line[0]]
        line[0] += 1
        return text

    for i in range(num_cases):
        D, N = map(int, next_line().split())
        h_list = []
        for _ in range(N):
            K, M = map(int, next_line().split())
            h_list.append((K, M))
        output.append("Case #%d: " % (i + 1) + str(solve(D, N, h_list)))

    with open(fname + '.out', 'w') as f:
        f.write('\n'.join(output))
