import sys

def rr(num):
    newnum = int(num*10000000+0.5)
    return float(newnum)/10000000.0

def main():
    f = open(sys.argv[1], "r")
    t = int(f.readline().strip())

    f2 = open(sys.argv[2], "w")

    for i in range(t):
        f2.write("Case #"+str(i+1)+": ")
        line = f.readline().strip().split()
        c = float(line[0])
        ff = float(line[1])
        x = float(line[2])

        cur = 0.0
        s = 2.0
        t = 0.0
        while cur < x:
            if x-cur <= c:
                t += (x-cur)/s
                break
            cur += c
            t += c/s
            rem = x-cur

            if rem/s >= (rem+c)/(s+ff):
                cur -= c
                s += ff

        f2.write(str(rr(t)))
        f2.write("\n")

    f.close()
    f2.close()

if __name__ == "__main__":
    main()
