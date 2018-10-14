import sys

def do_test_case(fd):
    tokens = fd.readline()

    num = int(tokens)
    ans = None

    while num >= 0:
        ans = num
        num_str = str(num)

        last_c = None
        for c in str(num):

            if last_c is not None and int(last_c) > int(c):
                ans = None
                break

            last_c = c

        if ans is not None:
            print ans
            break
        else:
            num -= 1


##################
file = sys.argv[1]

fd = open(file, 'r')

num_tests = fd.readline()

for i in xrange(1,int(num_tests)+1):
    sys.stdout.write("Case #%d: " % (i))
    do_test_case(fd)

