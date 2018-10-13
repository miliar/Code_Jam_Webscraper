from string import ascii_lowercase
import sys

def check_recycle(n, m):
    n = str(n)
    m = str(m)
    if len(n) <> len(m):
        return 0
    t = n + n
    if t.find(m) > -1:
        return 1
    return 0

def process(A, B):
    count = 0
    for n in range(A,B):
        for m in range(n+1, B+1):
            val = check_recycle(n,m)
            if val:
                count += val
    return count


if __name__ == '__main__':
    fname = sys.argv[1]
    rf = open(fname + '.in', 'r')
    of = open(fname + '.out', 'w')
    tt = int(rf.readline())
    for t in range(tt):
        input = rf.readline().strip()
        arr = input.split(' ')
        A,B = int(arr[0]), int(arr[1])
        output = process(A,B)
        of.write('Case #%d: %d\n' % (t+1, output))
    
        

