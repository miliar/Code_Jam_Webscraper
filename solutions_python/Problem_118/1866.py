import string

def main():

    infile = open('a.in','r')
    outfile = open('a.out','w')

    list_of_roots = open('list_of_roots', 'r')
    
    squares = []
    for s in list_of_roots:
        x = [int(s)**2] if len(s) > 0 else []
        print s
        squares += x
    
    T = int(string.strip(infile.readline()))    

    for k in xrange(T):
        print k
        A,B = map(int,string.strip(infile.readline()).split())
        
        r = range(A, B+1)
        answer = sum([1 if (x >= A and x <= B) else 0 for x in squares])

        outfile.write('Case #%d: %s\n' % (k+1,answer))


if __name__ == '__main__':
    main()

