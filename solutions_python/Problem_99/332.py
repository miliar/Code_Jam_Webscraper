def num_stroke(bin_repr, A, B):
    if bin_repr.find('0') == -1:
        return [B-A+1 + 2 * i for i in range(A+1)] + [B+2]
    else:
        l = []
        first_wrong = bin_repr.find('0')
        for i in range(A+1):
            if i < A-first_wrong:
                l.append(B+1+1+2*i+B-A)
            else:
                l.append(2*i+B-A+1)
        l.append(B+2)
        return l

def compute(bin_repr, p):
    res = 1
    for i in range(len(bin_repr)):
        if bin_repr[i] == '0':
            res *= (1-p[i])
        else:
            res *= p[i]
    return res

if __name__ == '__main__':
    #f = open('sample.in')
    #output= open('sample.out', 'w')
    f = open('A-small-attempt0.in')
    output = open('A-small.out', 'w')
    test_case = int(f.readline())
    for i in range(test_case):
        line = f.readline()
        line = line.split()
        A = int(line[0])
        B = int(line[1])
        line = f.readline()
        line = line.split()
        all_p = {}
        stroke_d = {}
        s = 'Case #%s: ' %(i+1)
        p = [float(line[j]) for j in range(A)]
        min_number = 2147483647
        for j in range(2**A):
            bin_repr = bin(j)[2:]
            if len(bin_repr) < A:
                bin_repr = '0'*(A-len(bin_repr)) + bin_repr
            all_p[bin_repr] = compute(bin_repr, p)
            stroke_d[bin_repr] = num_stroke(bin_repr, A, B)
        for j in range(A+2):
            expect = 0
            for k in range(2**A):
                bin_repr = bin(k)[2:]
                if len(bin_repr) < A:
                    bin_repr = '0'*(A-len(bin_repr)) + bin_repr
                expect += all_p[bin_repr] * stroke_d[bin_repr][j]
            if expect < min_number:
                min_number = expect
        output.write(s + str(min_number) + '\n')
    f.close()
    output.close()
