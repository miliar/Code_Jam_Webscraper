import string

def how_many_with_result(a, b):
    n,x = 0,a
    while x <= b:
        x = 2*x - 1
        n += 1
    return n, x
    

def solve(A, other_motes):
    if A == 1:
        return len(other_motes)
    if len(other_motes) == 0:
        return 0
    n, x = how_many_with_result(A, other_motes[0])
    return min(len(other_motes), n + solve(x + other_motes[0], other_motes[1:]))
    


def main():

    infile = open('a.in','r')
    outfile = open('a.out','w')

    T = int(string.strip(infile.readline()))    

    for k in xrange(T):
        print k
        A, N = map(int,string.strip(infile.readline()).split())
        other_motes = map(int,string.strip(infile.readline()).split())
        other_motes.sort()

        answer = solve(A, other_motes)

        outfile.write('Case #%d: %s\n' % (k+1,answer))


if __name__ == '__main__':
    main()

