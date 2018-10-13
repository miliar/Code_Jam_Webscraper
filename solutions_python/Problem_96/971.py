import sys

dict_n = {}
dict_s = {}

def result(str):
    values = str.split()
    ts = values[3:]

    n, s, p = int(values[0]), int(values[1]), int(values[2])

    y = 0
    ey = 0
    for i in range(n):
        t = int(ts[i])
        
        if (dict_n[t] >= p):
            y += 1
        elif (dict_s.has_key(t) and dict_s[t] >= p):
            ey += 1

    if (s >= ey):
        y += ey
    else:
        y += s
    
    return y

def main():
    fi = file(sys.argv[1], "r")
    fo = open(sys.argv[2], "w")

    for t in range(0, 31):
        d, r = t / 3, t % 3
        if r == 0:
            dict_n[t] = d
            if d > 0:
                dict_s[t] = d + 1
        elif r == 1:
            dict_n[t] = d + 1
        elif r == 2:
            dict_n[t] = d + 1
            dict_s[t] = d + 2

    print dict_n
    print dict_s
    T = int(fi.readline().strip())
    for t in range(1, T + 1):
        fo.writelines("Case #%d: %d\n" % (t, result(fi.readline().strip())))

if __name__ == "__main__":
    main()