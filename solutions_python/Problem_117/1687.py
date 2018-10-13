import sys
import logging
import os.path

def setup_logging():
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(levelname)-8s %(message)s')
    console.setFormatter(formatter)

    logger = logging.getLogger('flood')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(console)

setup_logging()
logger = logging.getLogger('flood')


def solve(a, copy_a, copy_b,  xs, ys):

    for x in range(xs):
        highest = None
        for y in range(ys):
            if not highest:
                highest = a[x][y]
            elif a[x][y] > highest:
                highest = a[x][y]
        
        for y in range(ys):
            copy_a[x][y] = highest

    logger.debug("copy_a: %s" % copy_a)

    for y in range(ys):
        direction = None
        highest = None
        for x in range(xs):
            if not highest:
                highest = a[x][y]
            elif a[x][y] > highest:
                highest = a[x][y]
        
        for x in range(xs):
            copy_b[x][y] = highest

    logger.debug("copy_b: %s" % copy_b)


    for x in range(xs):
        for y in range(ys):
            if min(copy_a[x][y], copy_b[x][y]) != a[x][y]:
                return False


    return True



            

if __name__ == "__main__":

    input_file = sys.argv[1]
    logger.info(input_file)

    if not os.path.isfile(input_file):
        logger.error("%s not a file" % input_file)
        sys.exit(1)

    fh = open(input_file, 'r')
    num_test_cases = int(fh.readline().strip())
    logger.debug("%s test cases" % num_test_cases)


    result = {True: 'YES',
              False: 'NO'}

    for test_case in range(num_test_cases):
        case_string = "Case #%s:" % (test_case + 1)
        logger.debug(case_string)
        x, y = fh.readline().strip().split(' ')
        x = int(x)
        y = int(y)
        logger.debug("x: %s, y: %s" % (x, y))
        
        a = [[0 for i in range(y)] for l in range(x)]
        copy_a = [[0 for i in range(y)] for l in range(x)]
        copy_b = [[0 for i in range(y)] for l in range(x)]
        logger.debug(a)

        for x2 in range(x):
            c1 = fh.readline().strip().split(' ')
            logger.debug(c1)
            for y2 in range(y):
                a[x2][y2] = (c1[y2])

        logger.debug("a: %s" % a)

        print "%s %s" % (case_string, result[solve(a, copy_a, copy_b, x, y)])
        
    fh.close() 

