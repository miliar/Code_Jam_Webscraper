import sys

def cookie(c,f,x):
    maximum = x/2.0
    if c >= x:
        return maximum
    n = 1.0
    minimum = float("inf")
    while True:
        time = 0.0
        for i in range(int(n)):
            time += c/(2.0+float(i)*f)
        time += x/(2.0+n*f)
        if time < minimum:
            minimum = time
        if time > minimum:
            break
        if time >= maximum:
            if maximum < minimum:
                minimum = maximum
            break
        n += 1.0
    return minimum

def main(argv = None):
    if argv is None:
        argv = sys.argv
    if (len(argv) != 3):
        print(len(argv))
        print("Wrong number of arguments")
        return
    fin = open (argv[1], 'r')
    lines = fin.readlines()
    CaseNum = int(lines[0])
    origin_stdout = sys.stdout
    w = open (argv[2], 'w')
    sys.stdout = w
    for i in range(CaseNum):
        inline1 = lines[i+1].strip().split()
        c = float(inline1[0])
        f = float(inline1[1])
        x = float(inline1[2])
        time = cookie(c,f,x)
        print("Case #%s:"  %(i+1), "%.7f" %time)
    sys.stdout = origin_stdout
    w.close()
    fin.close()
    return

if __name__ == '__main__':
    main()
