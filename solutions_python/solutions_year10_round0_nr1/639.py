def main():
    filename = 'small.in'
    
    inf = open(filename, 'r')
    outf = open(filename + '.out', 'w')
    for i, line in enumerate(inf):
        if i == 0:
            continue
        values = line.split()
        if len(values) == 2:
            N = int(values[0])
            K = int(values[1])
        else:
            continue
        mask = (1 << N) - 1
        if (mask & K) == mask:
            buf = 'Case #%d: ON\n' % i
        else:
            buf = 'Case #%d: OFF\n' % i
        outf.write(buf)
    inf.close()


if __name__ == '__main__':
    main()
    
