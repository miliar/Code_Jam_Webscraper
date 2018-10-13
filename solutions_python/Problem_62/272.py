def read_int_line(f):
    return int(f.readline().replace("\n",""))

def read_func_arr(func, f):
    return [func(b) for b in f.readline().replace("\n", "").split(" ")]

def read_int_arr(f):
    return read_func_arr(int, f)

def read_str(f):
    return f.readline().replace("\n", "")

def main(inf, outf):
    fr = open(inf)
    fw = open(outf, 'w')
    T = read_int_line(fr)
    for j in range(T):
        N = read_int_line(fr)
        ab = []
        for k in range(N):
            a, b = read_int_arr(fr)
            ab.append((a, b))
        print j
        res = "Case #%d: %d\n" % (j+1, result(ab))
        fw.write(res)
    fw.close()
    fr.close()

def result(pairs):
    c = 0
    start = True
    while pairs:
        a, b = pairs[0]
        
        for aj, bj in pairs:
            if (aj > a and bj < b) or (aj < a and bj > b):
                c += 1

        del pairs[0]
        start = False
    return c

if __name__ == "__main__":
    main('A-large.in', 'A.out')