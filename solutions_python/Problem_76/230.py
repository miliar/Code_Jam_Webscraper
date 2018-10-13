def main():
    filename = 'C-large'
    
    inf = open(filename + '.in', 'r')
    outf = open(filename + '.out', 'w')
    for i, line in enumerate(inf):
        values = line.split()
        if i == 0:
            T = int(values[0]) # number of test cases
            print 'T: %d' % T
            continue
        if i % 2 == 1:
            N = int(values[0])
            continue
        else:
            C = [int(j) for j in values]
        
        print N, C
        
        realSum = 0
        dummySum = 0
        min = 1000000
        
        for c in C:
            realSum += c
            dummySum ^= c
            if min > c:
                min = c
        
        if dummySum != 0:
            buf = 'Case #%d: NO\n' % int(i / 2)
        else:
            buf = 'Case #%d: %d\n' % (int(i / 2), realSum - min)
            print bin(dummySum ^ min)
            print bin(min)
        
        print buf,
        outf.write(buf)
    inf.close()


if __name__ == '__main__':
    main()
    
