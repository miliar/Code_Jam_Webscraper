def main():
    with open("b.txt", "r") as fin:
        with open("b.out", "w") as fout:
            fin.readline()
            case = 1
            for line in fin:
                n = int(line)
                rv = toTidy(n)
                fout.write("Case #{0}: {1}\n".format(case, rv))
                case += 1
    return

def isTidy(n):
    a = str(n)
    m = a[0]
    for i in range(0, len(a)):
        if a[i] < m:
            return False
        m = a[i]
    return True

def toTidy(n):
    pos = 0
    mul = 1
    while not isTidy(n):
        i = (n // mul) % 10
        if i != 9:
            n -= (i + 1) * mul
        pos += 1
        mul *= 10
    return n

if __name__ == "__main__":
    main()
