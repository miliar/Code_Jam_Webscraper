

def solve(R, C, A):
    badrow = set()
    for r, row in enumerate(A):
        if set(row) != {'?'}:
            for c, val in enumerate(row):
                if val != '?':
                    c2 = c
                    while c2 - 1 >= 0 and A[r][c2-1] == '?':
                        c2 -= 1
                        A[r][c2] = val
            latest = '?'
            for c, val in enumerate(row):
                if val != '?': latest = val
            if latest != '?':
                for c, val in enumerate(row):
                    if val == '?':
                        A[r][c] = latest
        else:
            badrow.add(r)
    #At this point we have horizontally filled in nonempty rows
    for r, row in enumerate(A):
        if r in badrow:
            for r2 in xrange(r, R):
                if r2 not in badrow:
                    break
            else:
                break
            row = A[r2]
            for r1 in xrange(r, r2):
                A[r1] = row

    #And catch the ending
    for r, row in enumerate(A):
        if set(row) != {'?'}:
            latest = row

    for r, row in enumerate(A):
        if set(row) == {'?'}:
            A[r] = latest
            
    return "\n".join("".join(row) for row in A)
            
###
def main():
    with open('in.txt','r') as fi, \
            open('out.txt', 'w') as fo:
        rr = lambda: fi.readline().strip()
        rrM = lambda: map(int,rr().split())
        for tc in xrange(1, 1 + int(rr())):
            R,C = rrM()
            A = [list(rr()) for _ in xrange(R)]
            zeta = solve(R, C, A)

            outstr = "Case #%i:\n" % tc + str(zeta)
            print outstr
            fo.write(outstr+'\n')
            
if __name__ == "__main__": main()
