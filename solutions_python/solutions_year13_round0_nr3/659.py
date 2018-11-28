import sys
import urllib2

def main():
    seq_text = urllib2.urlopen('http://oeis.org/A057136/b057136.txt').read()
    numbers = [int(line.split(' ')[1]) for line in seq_text.split('\n') if line.strip('\r\n') != '']
    tests = int(raw_input())
    for zzz in xrange(tests):
        a, b = (int(x) for x in raw_input().split(' '))
        res = sum((1 for x in numbers if x >= a and x <= b))
        print 'Case #{0}: {1}'.format(zzz + 1, res)

if __name__ == '__main__':
    main()
