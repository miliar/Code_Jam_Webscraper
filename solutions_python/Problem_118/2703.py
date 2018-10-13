import sys
import logging
import os.path
import math
def setup_logging():
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(levelname)-8s %(message)s')
    console.setFormatter(formatter)

    logger = logging.getLogger('flood')
    logger.setLevel(logging.INFO)
    logger.addHandler(console)

setup_logging()
logger = logging.getLogger('flood')

def check_palindrome(i):
    logger.debug("Checking palindrome: %s" % i)
    s = "%s" % i
    le = len(s)
    half = le / 2
    for x in range(half):
        if s[x] != s[le - x - 1]:
            return False

    logger.debug("...yup!")
    return True

def perm(s, length, stop, position, min_v, max_v, last_number = None):
    ret = 0
    for x in range(10):
        if position == 0 and x == 0:
            continue
        s[position] = str(x)

        s[length - position - 1] = str(x)
        num = int(''.join(s))

        if position +1 == stop:
            logger.debug(s)            
            sqrt = int(math.sqrt(num))
            if num != last_number and num <= max_v and num >= min_v and sqrt * sqrt == num and check_palindrome(sqrt):
                logger.info("YAY: %s (%s)" % (num, sqrt))
                ret += 1
        if position + 1 < stop:
            ret += perm(s, length, stop, position + 1, min_v, max_v, last_number = num)
    return ret

def find_ps(length, min_v, max_v):

    s = ['0' for x in range(length)]
    return perm(s, length, length / 2 + (length % 2), 0, min_v, max_v)

if __name__ == "__main__":

    input_file = sys.argv[1]
    logger.info(input_file)

    if not os.path.isfile(input_file):
        logger.error("%s not a file" % input_file)
        sys.exit(1)

    fh = open(input_file, 'r')
    num_test_cases = int(fh.readline().strip())
    logger.debug("%s test cases" % num_test_cases)


    for test_case in range(num_test_cases):
        case_string = "Case #%s:" % (test_case + 1)
        logger.debug(case_string)
        x, y = fh.readline().strip().split(' ')
        min_lengths = len(x)
        max_lengths = len(y)
        x = int(x)
        y = int(y)
        logger.debug("x: %s, y: %s" % (x, y))
        logger.debug("lengths: %s %s" % (min_lengths, max_lengths))

        total = 0        
        for length in xrange(min_lengths, max_lengths + 1):
            logger.debug("doing length %s" % length)
            total += find_ps(length, x, y)

        logger.info("%s %s-%s %s" % (case_string, x, y, total))
        print "%s %s" % (case_string, total)
        
    fh.close() 

