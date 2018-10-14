def comp(a):
    t = a[0]
    tlen = len(t)

    for i in range(1, len(a)):
        if tlen != len(a[i]):
            return False

        for j in range(tlen):
            if t[j][0] != a[i][j][0]:
                return False

    return True


def work(case_vars):
    n, s = case_vars

    d = []
    for i in range(n):
        prev = s[i][0]
        word = s[i]
        index = 0
        d.append([[prev, 1]])
        for j in range(1, len(word)):
            if word[j] == prev:
                d[i][index][1] += 1
            else:
                prev = word[j]
                index += 1
                d[i].append([prev, 1])

    if not comp(d):
        return "Fegla Won"

    c = 0
    s = [0]*len(d[0])
    s2 = [0]*len(d[0])
    res = [0]*len(d[0])
    for i in range(len(d)):
        w = d[i]
        for j in range(len(w)):
            l = w[j]
            s[j] += l[1]

    for w in d:
        for i in range(len(w)):
            res[i] += abs(s[i]/n - w[i][1])

    return sum(res)


def get_cases(f):
    #read num of cases
    cases = int(f.readline())
    for case in range(cases):

        n = int(f.readline().strip())
        s = [f.readline().strip() for _ in range(n)]

        yield case+1, n, s


def main():
    flag = 1

    input_name = "test.in" if flag == 0 else "A-small-attempt0.in" if flag == 1 else "A-large.in"
    output_name = input_name[:-2] + "out"
    print input_name
    print output_name

    with open(input_name, 'rb') as in_file,  open(output_name, 'w') as out_file:
        for case_vars in get_cases(in_file):
            case = case_vars[0]
            print case
            c = work(case_vars[1:])
            to_w = "Case #%d: %s" % (case, c) + "\n"
            out_file.write(to_w)

main()
