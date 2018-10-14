import sys

def main():
    with sys.stdin as f:
        for x in range(int(f.readline())):
            solve(f, x+1)

def solve(f, case):
    data = f.readline().split(' ')
    Astr = data[0]
    A = int(Astr)
    Bstr = data[1]
    B = int(Bstr)
    l = len(data[0])
    n = A
    count = 0
    while n <= B:
        nstr = str(n)
        nm = []
        for i in range(1, l):
            if nstr[i] < nstr[0] or nstr[i] > Bstr[0]:
                continue
            mstr = ''.join((nstr[i:], nstr[:i]))
            if (mstr > nstr and mstr <= Bstr 
                    and mstr[0] != '0'
                    and (nstr, mstr) not in nm):
                nm.append((nstr, mstr))
                count += 1
        n += 1
    print 'Case #%d: %d' % (case, count)

if __name__ == '__main__':
    main()
