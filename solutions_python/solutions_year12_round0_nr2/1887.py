def main(filename):
    file = open(filename, 'r')
    outf = open('output.txt', 'w')
    numcases = int(file.readline())
    for i in range(numcases):
        items = file.readline().split()
        n = int(items[0])
        s = int(items[1])
        p = int(items[2])
        res = 0
        close = 0
        for a in range(n):
            t = int(items[a+3])
            lower = (p-1) * 3
            if p == 0:
                res += 1
            elif t > lower:
                res += 1
            elif t == lower and t > 0:
                close += 1
            elif lower > 0 and lower-t == 1 and t > 0:
                close += 1
        res += min(close, s)
        outf.write('Case #' + str(i+1) + ': ' + str(res) + '\n')

if __name__ == '__main__':
    main('B-large.in')
