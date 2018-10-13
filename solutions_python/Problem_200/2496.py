def check_tidy(num):
    """    
    :param num: 
    :return: -1 if tidy, otherwise the breaking index 
    """
    digits = [int(x) for x in str(num)]
    for i in xrange(len(digits)-1, 0, -1):
        if digits[i] < digits[i-1]:
            return i
    return -1


def solve_case(n):
    i = check_tidy(n)
    while i != -1:
        n_upper = str(n)[:i]
        n_lower = str(n)[i:]
        n = int(str(int(n_upper) - 1) + '9' * len(n_lower))
        i=check_tidy(n)
    return n


def solve_from_file(infile, outfile):
    fin = open(infile, 'rb')
    fout = open(outfile, 'wb')
    t = int(fin.readline())
    res = []
    for i in xrange(t):
        n = fin.readline()
        res.append("Case #{i}: {res}\n".format(
            i=i+1,
            res=solve_case(int(n))
        ))
    fout.writelines(res)

if __name__ == "__main__":
    solve_from_file("/Users/yoni/Downloads/B-large.in", "/Users/yoni/Downloads/B-large.out")
