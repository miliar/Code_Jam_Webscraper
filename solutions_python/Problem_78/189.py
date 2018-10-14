import sys
from fractions import Fraction

def process_file( fin, fout ):
    def get_one_problem():
        N, PD, PG = map( int, fin.readline().split() )
        return (N,PD,PG)

    num_cases = int( fin.readline() )
    for i in range( num_cases ):
        N, PD, PG = get_one_problem()
        s = solve_one_problem( N, PD, PG )
        fout.write( "Case #%d: %s\n" % (i+1,s) )

def solve_one_problem( N, PD, PG ):
    if ( (PG==100) and (PD < 100)):
        return "Broken"
    if ( (PG==0) and (PD > 0)):
        return "Broken"
    if (Fraction(PD,100).denominator > N):
        return "Broken"
    return "Possible"

process_file( open(sys.argv[1]), open(sys.argv[1].replace("in", "out"), "w") )
