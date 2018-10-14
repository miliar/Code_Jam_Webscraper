import sys

def read_board(fd):
    first_ans = int(fd.readline())
    row = []
    row.append( fd.readline().split() )
    row.append( fd.readline().split() )
    row.append( fd.readline().split() )
    row.append( fd.readline().split() )

    return row[first_ans-1]

def do_test_case(fd):
    a = read_board(fd)
    b = read_board(fd)

    c = set(a).intersection( set(b) )

    len_c = len(c)

    if not len_c:
        print "Volunteer cheated!"
    elif len_c == 1:
        print c.pop()
    else:
        print "Bad magician!"


file = sys.argv[1]

fd = open(file, 'r')

num_tests = fd.readline()

for i in xrange(1,int(num_tests)+1):
    sys.stdout.write("Case #"+str(i)+": ")
    do_test_case(fd)

