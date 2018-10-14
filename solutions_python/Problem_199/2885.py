def main():
    with open("a.txt", "r") as fin:
        with open("a.out", "w") as fout:
            fin.readline()
            case = 1
            for line in fin:
                (pan, k) = line.split(" ")
                rv = panFlip(toArray(pan), int(k))
                if rv == -1:
                    fout.write("Case #{0}: IMPOSSIBLE\n".format(case))
                else:
                    fout.write("Case #{0}: {1}\n".format(case, rv))
                case += 1
    return

def toArray(s):
    a = []
    for c in s:
        if c == '+':
            a.append('+')
        else:
            a.append('-')
    return a

def panFlip(a, k):
    s = len(a)
    counter = 0
    for i in range(0, s-k):
        if a[i] == '+':
            continue
        counter += 1
        a[i] = '+'
        for j in range(i+1, i+k):
            if a[j] == '+':
                a[j] = '-'
            else:
                 a[j] = '+'
    if a[s-k] == "+":
        #check all plus
        for i in range(s-k+1, s):
            if a[i] != '+':
                return -1
    else:
        #check all minus
        counter += 1
        for i in range(s-k+1, s):
            if a[i] != '-':
                return -1
    
    return counter

if __name__ == "__main__":
    main()
