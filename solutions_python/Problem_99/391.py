import sys

def read_line_from_file():
    return str(sys.stdin.readline()).strip()

def get_prob(i, n, percent):

    return

def solve(n_typed, n_total, percent):
    t = n_typed
    n = n_total
    key_num_list = []
    key_num_list.append(t + n + 1)  # backspace t times
    key_num_list.append(n + 2)      # just enter

    for i in range(t):  # 0 ~ t-1
        # i: back space number
        correct = t - i
        tp = 1
        for j in range(correct):
            tp *= percent[j]
        ck = i + (n - (t - i)) + 1
        wk = i + (n - (t - i)) + 1 + n + 1
        k = tp * ck + (1 - tp) * wk
        #print tp, ck, wk, k
        key_num_list.append(k)
    #print key_num_list
    return min(key_num_list)

if __name__ == '__main__':
    fout = open("%s.out" % (sys.argv[0]), "w")
    num = int(read_line_from_file())
    for i in range(num):
        line = map(int, read_line_from_file().split(' '))
        n_typed, n_total = line[0], line[1]
        #print n_typed, n_total
        percent = map(float, read_line_from_file().split(' '))  # correctly typed
        #print percent
        res = solve(n_typed, n_total, percent)
        fout.write("Case #%d: %.6f\n" % (i + 1, res))
    fout.close()