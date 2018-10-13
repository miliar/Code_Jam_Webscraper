import sys, copy;

r, c, m = 0, 0, 0

def empties(count) :
    return "." * count;    


def mines(count) :
    return "*" * count;    


def c_empty_line() :
    return "c" + empties(c - 1) + "\n";


def empty_lines(count) :
    return (empties(c) + "\n") * count;


def c_mine_line() :
    return "c" + mines(c - 1) + "\n";


def mine_lines(count) :
    return (mines(c) + "\n") * count;


def ii_mines(count) :
    return (".." + mines(c - 2) + "\n") * count;


def mixed(one, two, count2, three, count3) :
    print one + two * count2 + three * count3;
    return one + two * count2 + three * count3;


def solve() :
    global r, c, m;
    if ( m == 0 ) :
        return c_empty_line() + empty_lines(r - 1);
    
    if ( m == r * c - 1 ) :
        return c_mine_line() + mine_lines(r - 1);
    
    if ( r == 1 ) :
        return "c" + empties(c - m - 1) + mines(m) + "\n";
    
    if ( c == 1 ) :
        return mixed("c\n", ".\n", r - m - 1, "*\n", m);
    
    if ( ( ( ( r == 2 ) or ( c == 2 ) ) and ( m % 2 == 1 ) ) or ( ( r == 2 ) and ( ( m >> 1 ) == c - 1 ) ) or ( ( c == 2 ) and ( ( m >> 1 ) == r - 1 ) ) ) :
        return "Impossible\n";
    
    if ( r == 2 ) :
        m = m >> 1;
        return "c" + empties(c - m - 1) + mines(m) + "\n" + empties(c - m) + mines(m) + "\n";
    
    if ( c == 2 ) :
        m = m >> 1;
        return mixed("c.\n", "..\n", r - m - 1, "**\n", m);
    
    v = r * c - m;
    if ( v == 4 ) :
        return "c." + mines(c - 2) + "\n.." + mines(c - 2) + "\n" + mine_lines(r - 2);
    
    if ( v == 6 ) :
        return "c.." + mines(c - 3) + "\n..." + mines(c - 3) + "\n" + mine_lines(r - 2);
    
    if ( v < 8 ) :
        return "Impossible\n";
    
    w = v - 8;
    x = w >> 1;
    y = w % 2;
    print "x " + str(x);
    print "y " + str(y);
    if ( x <= c - 3 ) :
        return "c.." + empties(x) + mines(c - x - 3) + "\n..." + empties(x) + mines(c - x - 3) + "\n.." + ('.' if ( y == 1 ) else '*') + mines(c-3) + "\n" + mine_lines(r-3);
    
    x = x - c + 3;
    print "x " + str(x);
    if ( x <= r - 3 ) :
        return c_empty_line() + empty_lines(1) + ".." + ('.' if ( y == 1 ) else '*') + mines(c - 3) + "\n" + ii_mines(x) + mine_lines(r - x - 3);
    
    x = x - r + 3;
    print "x " + str(x);
    w = ( x << 1 ) + y;
    a = w / ( c - 2 );
    b = w % ( c - 2 );
    print "a " + str(a);
    print "b " + str(b);
    return c_empty_line() + empty_lines(a + 1) + empties(b + 2) + mines(c - b - 2) + "\n" + ii_mines(r - a - 3);
   

inputFile =  sys.argv[1] if (len(sys.argv) > 1) else "input.txt";
outputFile = sys.argv[2] if (len(sys.argv) > 2) else (inputFile + "out.txt") if (len(sys.argv) > 1) else "output.txt";
print inputFile, outputFile
file = open(outputFile, "w")

with open(inputFile, 'r') as cin:
    t = int(cin.readline())
    print t
    for i in range(1, t + 1):
        file.write("Case #" + str(i) + ": \n")
        r, c, m = map(int, cin.readline().split())
        file.write(str(solve()))
file.close()            








