#fin = "small.in"
#fout = "small.out"

fin = "large.in"
fout = "large.out"

def chop_data(s):
    s = s.strip()
    s = s.split()
    n = int(s[0])
    sup = int(s[1])
    p = int(s[2])
    T = []
    check = []
    for i in range(0,n):
        T.append(int(s[i+3]))
    return (n, sup, p, T)

def check_data_1(n, sup, p, T):

    result = 0
    for i in range(0,n):
        use = False
        if T[i] % 3 == 1:
            max_val = T[i] / 3 + 1
        elif T[i] % 3 == 2:
            use = True
            max_val = T[i] / 3 + 1
        else:
            use = True
            max_val = T[i] / 3

        if max_val >= p:
            result += 1
        else:
            if use and sup > 0:
                if max_val < T[i]:
                    if max_val + 1 >= p:
                        result += 1
                        sup -= 1
    return result

if __name__ == "__main__":
    f_in = open(fin)
    f_out = open(fout,'w')
    test_cases = int(f_in.readline())
    for t in range(0,test_cases):
        s = f_in.readline()
        n, sup, p, T = chop_data(s)
        result = check_data_1(n, sup, p, T)
        s2 = "Case #" + str(t + 1) + ": " + str(result) + "\n"
        f_out.write(s2)
    f_in.close()
    f_out.close()
