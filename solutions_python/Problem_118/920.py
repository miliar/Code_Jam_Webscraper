import sys

def process_file( fin, fout ):
    def get_one_problem():
        A, B = map( int, fin.readline().split() )
        return (A, B)

    num_cases = int( fin.readline() )
    for i in range( num_cases ):
        A, B = get_one_problem()
        s = solve_one_problem( A, B )
        fout.write( "Case #%d: %s\n" % (i+1,s) )

def solve_one_problem( A, B ):
    count = 0
    for i in range( len( fs ) ):
        if fs[i] >= A and fs[i] <= B:
            count = count + 1
        if fs[i] > B:
            break
    return count

def generate_fs( M ):
    fs = []
    i = 1
    while True:
        isqr = i**2;
        if isqr > M:
            break;
        if str(i) == str(i)[::-1] and str(isqr) == str(isqr)[::-1]:
            fs.append( isqr )
        i = i+1
    return fs

fs = generate_fs( 10**14 )
print "Finished generation"
process_file( open(sys.argv[1]), open(sys.argv[1].replace("in", "out"), "w") )
