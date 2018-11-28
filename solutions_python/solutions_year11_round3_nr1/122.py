import sys

def readline():
    return sys.stdin.readline().strip()

def mark(p, r, c, R, C):
    p[r][c] = '/'
    if r < (R - 1) and p[r + 1][c] == '#':
        p[r + 1][c] = '\\'
    else:
        return False
    if c < (C - 1) and p[r][c+1] == '#':
        p[r][c + 1] = '\\'
    else:
        return False
    if p[r + 1][c+1] == '#':
        p[r+1][c+1] = '/'
    else:
        return False
    return True

def solve(R, C, p):
    #print_p(p)
    for r in range(R):
        for c in range(C):
            if p[r][c] == '#':
                #print_p(p)
                #print
                if not mark(p, r, c, R, C):
                    print "Impossible"
                    return
                #print_p(p)
                #print
    #print p
    # Check if any blues left
    for v in p:
        for v2 in v:
            if v2 == '#':
                print "Impossible"
                return
    print_p(p)

def print_p(p):
    for v in p:
        print "".join(v)

def main():
    n_inputs = int(readline())
    for i in range(n_inputs):
        R, C = [int(n) for n in readline().split()]
        picture = []
        for j in range(R):
            row = list(readline())
            picture.append(row)
        #print picture
        print "Case #%d:" % (i + 1) 
        solve(R, C, picture)

if __name__ == "__main__":
    main()
