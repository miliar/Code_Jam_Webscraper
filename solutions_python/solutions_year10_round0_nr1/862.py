# _*_ coding: utf-8 _*_
import sys

def main():
    count = 0
    if len(sys.argv) != 2:
        print 'Usage: python snapper_chain.py <filename>'
        exit()

    filename = sys.argv[1]
    try:
        f = open(filename, 'r')
    except IOError:
        print "Can not open '%s'." % filename
        exit()

    for line in f.readlines():
        n = k = ''
        if count == 0:
            count += 1
            continue

        n, k = line.split()
        result = 'ON' if (int(k) + 1) % (2 ** int(n)) == 0 else 'OFF'
        print 'Case #%d: %s' % (count, result)
        count += 1

if __name__ == '__main__':
    main()
