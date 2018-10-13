from math import sqrt

def isPalindrome(n):
    d = 0
    m = n
    while m:
        m /= 10
        d += 1

    c = d/2
    rdiv = 1
    ldiv = 10**(d-1)

    while c:
        if (n/ldiv)%10 != (n/rdiv)%10:
            return False
        rdiv *= 10
        ldiv /= 10
        c -= 1

    return True

def run(inpath, outpath):
    fin = open(inpath, 'rU')
    fout = open(outpath, 'w')

    case = 1
    for i, line in enumerate(fin):
        line = line.strip()
        if not i or not line:
            continue

        lower, upper = [int(x) for x in line.split(' ')]

        n = 0
        while lower <= upper:
            srt = sqrt(lower)
            isrt = int(srt)

            if srt == isrt:
                n += isPalindrome(lower) and isPalindrome(isrt)

            lower += 1

        cstr = 'Case #%d: %d\n'%(case, n)
        print cstr[:-1]
        fout.write(cstr)

        case += 1
