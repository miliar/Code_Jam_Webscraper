import sys

power = [10, 100, 1000, 10000, 100000, 1000000]

def result(str_line):
    values = str_line.split()
    A, B = int(values[0]), int(values[1])
    #print A, B
    #print "--------"

    l = []
    #count = 0;
    for x in range(A, B+1):
        d = 0

        for i in reversed(range(len(power))):
            if power[i] <= x and d == 0:
                d = i + 1

            if d > 0:
                t = x % power[i] * pow(10, d - i) + x / power[i]
                if t > x and t <= B:
                    #count += 1
                    #print x, t, i + 1
                    l.append(x * 10000 + t)

    return len(set(l))

    #return count

def main():
    fi = file(sys.argv[1], "r")
    fo = open(sys.argv[2], "w")

    T = int(fi.readline().strip())
    for t in range(1, T + 1):
        fo.writelines("Case #%d: %d\n" % (t, result(fi.readline().strip())))

if __name__ == "__main__":
    main()